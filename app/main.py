from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import users

app = FastAPI()


app.include_router(users.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
