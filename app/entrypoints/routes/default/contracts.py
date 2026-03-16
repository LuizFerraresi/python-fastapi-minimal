from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: str = "ok"

class HealthzResponse(BaseModel):
    healthy: bool = True

class WhoamiResponse(BaseModel):
    ip: str
    client: str
    user_agent: str
    headers: dict[str, str]
