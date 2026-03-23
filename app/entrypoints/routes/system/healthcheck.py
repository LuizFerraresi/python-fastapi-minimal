
from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR

from app.schemas.system import HealthzResponse
from app.domain.system import HealthcheckService

router = APIRouter(prefix="/health")


@router.get(path="/live", status_code=HTTP_200_OK, response_model=HealthzResponse)
async def liveness_probe_route():
    """Verify the process is responsive."""
    return HealthcheckService.ping()

@router.get(path="/ready", status_code=HTTP_200_OK, response_model=HealthzResponse)
async def readiness_probe_route():
    """Verify if dependencies are ready and reachable.

    A real world example should looks like the following:
    
    async def readiness_probe_route(
        database: Annotated[Database, Depends(get_database_session)],
        cache: Annotated[Cache, Depends(get_cache_session)],
        broker: Annotated[Broker, Depends(get_broker)],
    ):
        result = await HealthcheckService(database=database, cache=cache, broker=broker).readiness()
    """
    try:
        result = HealthcheckService().readiness()

    except Exception as e:
        return HTTPException(HTTP_500_INTERNAL_SERVER_ERROR, str(e))

    return {
        "status": result
    }
