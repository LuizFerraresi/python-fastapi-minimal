from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["System"])

__all__ = ["router"]
