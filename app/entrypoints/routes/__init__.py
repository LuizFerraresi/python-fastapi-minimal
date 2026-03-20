from fastapi import APIRouter

from app.entrypoints.routes.system import router as system

router = APIRouter(prefix="/api")
router.include_router(system)

__all__ = ["router"]
