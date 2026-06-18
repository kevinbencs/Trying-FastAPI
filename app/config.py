from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Setting(BaseSettings):
    database_url: str

    jwt_secret: str
    jwt_algorith: str = "HS256"
    jwt_expire_minutes: int =  60

    model_config = SettingsConfigDict(
        env_file = ".env"
        env_file_encodeing = "utf-8"
    )

@lru_cache
def get_settings() ->Settings:
    return Settings()