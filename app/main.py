from typing import Union

from supabase_client import get_supabase_client
from fastapi import Depends, FastAPI
from .routers import users

supabase_client = get_supabase_client()
app = FastAPI()



app.include_router(users.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
