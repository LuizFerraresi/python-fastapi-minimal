from fastapi import APIRouter

from .healthcheck import router as healthcheck
from .index import router as index
from .whoami import router as whoami

router = APIRouter(tags=["System"])
router.include_router(healthcheck)
router.include_router(index)
router.include_router(whoami)
