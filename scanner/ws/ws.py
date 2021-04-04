import json
import asyncio
import websockets
import requests

from web.db import database, users
from .settings import settings
from .on_open import on_open


class Client:
    def __init__(self, token_cb):
        self.ws = None
        self.token_cb = token_cb

    async def request(self, request_type: str, data: dict = None, get_data=True):
        request = {
            "type": request_type
        }
        if data:
            request["data"] = data
        print(request)
        await self.ws.send(json.dumps(request))
        return await self.recv(get_data)

    async def recv(self, get_data=True):
        res = json.loads(await self.ws.recv())
        print(res)
        if get_data:
            return res["data"]
        return res
    
    async def login(self):  # return created new scanner or not
        res = await self.request("login", {
            "uuid": settings.uuid,
            "password": settings.password
        }, False)
        if "error" in res and res["error"]:
            res = requests.post(settings.api, json={
                "uuid": settings.uuid,
                "password": settings.password
            }).json()
            print(res)
            return True
        return False

    async def run(self):
        try:
            async with websockets.connect(settings.url) as ws:
                self.ws = ws

                if await self.login():
                    await self.login()

                self.token_cb(await self.request("get_token"))

                while True:
                    data = await self.recv()
                    user = await database.fetch_one(users.select(users.c.user_id == data["user_id"]))
                    if user:
                        await on_open(user["user_id"])
        except BaseException as e:
            print(e)

    def run_sync(self):
        asyncio.run(self.run())
