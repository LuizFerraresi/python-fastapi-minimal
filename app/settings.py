from pydantic import Field
from pydantic_settings import BaseSettings

from functools import lru_cache


class ApplicationSettings(BaseSettings):
    name: str = Field(default=..., alias="APPLICATION_NAME")
    version: str = Field(default=..., alias="APPLICATION_VERSION")
    debug_enabled: bool = Field(default=False, alias="APPLICATION_DEBUG_ENABLED")


@lru_cache
def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
