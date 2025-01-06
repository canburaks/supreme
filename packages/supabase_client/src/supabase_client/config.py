from functools import lru_cache

from pydantic_settings import BaseSettings


class SupabaseSettings(BaseSettings):
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    class Config:
        env_file: str = ".env"
        extra: str = "allow"


@lru_cache()
def get_supabase_settings() -> SupabaseSettings:
    return SupabaseSettings()
