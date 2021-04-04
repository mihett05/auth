from pydantic import BaseModel
from typing import Union, Optional


class LoginData(BaseModel):
    uuid: str
    password: str


class CommandData(BaseModel):
    command: str = "open"
    user_id: int


class Message(BaseModel):
    type: str
    data: Union[LoginData, CommandData]


class Response(BaseModel):
    type: str
    data: Optional[Union[dict, list, str]]
    error: Optional[str]


class LoginMessage(Message):
    type: str = "login"
    data: LoginData


class CommandMessage(Message):
    type: str = "command"
    data: CommandData

    def __init__(self, user_id: int):
        super().__init__(**{
            "type": "command",
            "data": CommandData(command="open", user_id=user_id)
        })

