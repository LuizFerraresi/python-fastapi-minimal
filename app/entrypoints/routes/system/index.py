from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from app.schemas.system import IndexResponse
from app.settings import ApplicationSettings, get_settings
from app.domain.system import index

router = APIRouter()


@router.get(path="/index", status_code=HTTP_200_OK, response_model=IndexResponse)
async def index_route(settings: Annotated[ApplicationSettings, Depends(get_settings)]):
    """Expose index route."""
    return await index(settings)
