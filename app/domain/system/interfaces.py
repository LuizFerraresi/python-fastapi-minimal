from typing import Protocol


class ApplicationSettings(Protocol):
    name: str
    version: str


class Repository(Protocol):
    async def ping(self) -> bool:
        ...
