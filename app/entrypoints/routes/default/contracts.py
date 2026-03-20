from pydantic import BaseModel

from enum import Enum


class IndexResponse(BaseModel):
    name: str
    version: str


class HealthzStatus(Enum):
    OK = "ok"
    READY = "ready"
    NOT_READY = "not-ready"


class HealthzResponse(BaseModel):
    status: HealthzStatus


class WhoamiResponse(BaseModel):
    ip: str
    client: str
    user_agent: str
    headers: dict[str, str]
