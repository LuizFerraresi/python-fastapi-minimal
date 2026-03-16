from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter(prefix="/api", tags=["System"])

@router.get(path="/status")
async def status_route():
    return {"status": "ok"}

@router.get(path="/healthz")
async def healthz_route():
    return {"status": "ok"}

@router.get(path="/whoami")
async def whoami_route(request: Request):
    return {"status": "ok"}
