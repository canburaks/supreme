from typing import Union

from fastapi import FastAPI
from supabase_client import get_supabase_client

supabase_client = get_supabase_client()
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
