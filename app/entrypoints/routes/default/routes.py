from fastapi import APIRouter
from starlette.requests import Request

from .contracts import StatusResponse, HealthzResponse, WhoamiResponse

defaults = APIRouter(tags=["System"])

@defaults.get(path="/status", response_model=StatusResponse)
async def status_route():
    """Expose status endpoint"""
    return {"status": "ok"}

@defaults.get(path="/healthz", response_model=HealthzResponse)
async def healthz_route():
    """Expose helthz endpoint"""
    return {"healthy": True}

@defaults.get(path="/whoami", response_model=WhoamiResponse)
async def whoami_route(request: Request):
    """Expose whoami endpoint."""
    client_host = request.client
    forwarded_for = request.headers.get('x-forwarded-for')
    real_ip = forwarded_for.split(',')[0].strip() if forwarded_for else client_host
    user_agent = request.headers.get('user-agent', 'unknown')

    return {
        'ip': real_ip,
        'client': client_host,
        'user_agent': user_agent,
        'headers': dict(request.headers),
    }
