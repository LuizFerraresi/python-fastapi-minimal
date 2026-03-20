from pydantic import Field
from pydantic_settings import BaseSettings

from functools import lru_cache


class ApplicationSettings(BaseSettings):
    name: str = Field(default=..., alias="APPLICATION_NAME")
    version: str = Field(default=..., alias="APPLICATION_VERSION")


@lru_cache
def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
