from pydantic import Field
from pydantic_settings import BaseSettings

from functools import lru_cache


class ApplicationSettings(BaseSettings):
    name: str = Field(default=...)
    version: str = Field(default=...)
    debug_enabled: bool = Field(default=False)


@lru_cache
def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
