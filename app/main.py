from typing import Union
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import users

import supabase_client

app = FastAPI()



app.include_router(users.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



app.mount(path="/supabase", app=supabase_client.app)
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
