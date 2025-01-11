import os
from typing import Any, Union, Annotated
from fastapi import Depends, Request
from pydantic import Field
from supabase import Client, create_async_client, create_client
from supabase._async.client import AsyncClient as AsyncClient
from functools import lru_cache

from .config import get_supabase_settings


@lru_cache()
def get_supabase_client() -> Client:
    """
    Get a supabase async client.
    """
    settings = get_supabase_settings().model_dump()
    url: Union[str, None] = settings["SUPABASE_URL"]
    key: Union[str, None] = settings["SUPABASE_KEY"]
    if not url or not key:
        raise ValueError("SUPABASE_URL or SUPABASE_KEY is not set")

    supabase_client: Client = create_client(supabase_url=url, supabase_key=key)

    return supabase_client


@lru_cache()
async def get_supabase_aclient() -> AsyncClient:
    """
    Get a supabase async client.
    """
    settings = get_supabase_settings().model_dump()
    url: Union[str, None] = settings["SUPABASE_URL"]
    key: Union[str, None] = settings["SUPABASE_KEY"]
    if not url or not key:
        raise ValueError("SUPABASE_URL or SUPABASE_KEY is not set")
    supabase = create_async_client(supabase_url=url, supabase_key=key)

    return await supabase


async def get_client() -> Client:
    client = get_supabase_client()
    return client


ClientDep = Depends(get_client)
