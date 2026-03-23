from fastapi import APIRouter
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.schemas.system import WhoamiResponse
from app.domain.system import whoami

router = APIRouter()


@router.get(path="/whoami", status_code=HTTP_200_OK, response_model=WhoamiResponse)
async def whoami_route(request: Request):
    """Expose Who am I endpoint."""
    return await whoami(str(request.client), dict(request.headers))
