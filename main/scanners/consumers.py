import aioredis
import jwt

from django.conf import settings

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import Scanner
from .messages import LoginMessage, CommandMessage, Response


@database_sync_to_async
def get_scanner(uuid, password):
    scanner = Scanner.objects.filter(uuid=uuid).first()
    if scanner and scanner.check_password(password):
        return scanner


class ScannerConsumer(AsyncJsonWebsocketConsumer):
    _redis = None

    @classmethod
    def redis(cls) -> aioredis.Redis:
        return cls._redis

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uuid = None

    async def connect(self):
        if not ScannerConsumer._redis:
            ScannerConsumer._redis = await aioredis.create_redis_pool("redis://localhost:6379")
        await self.channel_layer.group_add("scanner_command_group", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        if self.uuid:
            await self.redis().delete(self.uuid)
        await self.channel_layer.group_discard("scanner_command_group", self.channel_name)
        await self.close()

    async def send_model(self, model):
        return await self.send_json(model.dict())

    async def events_open(self, event):
        if event["data"]["uuid"] == self.uuid:
            await self.send_model(CommandMessage(event["data"]["user_id"]))

    async def receive_json(self, content, **kwargs):
        if "type" not in content:
            await self.send_json({
                "error": "You must provide type of a message"
            })
        elif content["type"] == "login":
            msg = LoginMessage(**content)
            scanner = get_scanner(msg.data.uuid, msg.data.password)
            if not scanner or bool(await self.redis().get(msg.data.uuid)):
                await self.send_model(Response(
                    type="login",
                    error="Can't login with provided credentials"
                ))
            else:
                await self.redis().set(msg.data.uuid, True)
                self.uuid = msg.data.uuid
                await self.send_model(Response(
                    type="login",
                    data="ok"
                ))
        elif content["type"] == "get_token":
            if not self.uuid:
                await self.send_model(Response(
                    type="get_token",
                    error="You haven't logged in"
                ))
            else:
                token = jwt.encode({
                    "uuid": self.uuid
                }, settings.SECRET_KEY, "HS256")
                await self.send_model(Response(
                    type="get_token",
                    data=token
                ))
        else:
            await self.send_model(Response(
                type=content["type"],
                error="Unknown content type"
            ))
