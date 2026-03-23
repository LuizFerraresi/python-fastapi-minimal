
from pydantic import BaseModel

from app.domain.system import HealthStatus


class IndexResponse(BaseModel):
    name: str
    version: str


class HealthzResponse(BaseModel):
    status: HealthStatus


class WhoamiResponse(BaseModel):
    ip: str
    client: str
    user_agent: str
    headers: dict[str, str]
