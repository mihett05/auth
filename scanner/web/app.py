from typing import List
from fastapi import FastAPI, Response

from .db import database, users
from .models import User

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def startup():
    await database.disconnect()


@app.get("/users", response_model=List[User])
async def get_users():
    return await database.fetch_all(users.select())


@app.post("/users", status_code=201)
async def create_user(user: User):
    if not await database.fetch_one(users.select(users.c.user_id == user.user_id)):
        await database.execute(users.insert().values(user_id=user.user_id))
        return Response(status_code=200)
    return Response(status_code=201)


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if await database.fetch_one(users.select(users.c.user_id == user_id)):
        await database.execute(users.delete().where(users.c.user_id == user_id))
    return Response()
