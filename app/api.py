from fastapi import FastAPI

from .settings import get_settings, ApplicationSettings
from .entrypoints.routes import router

def application(settings: ApplicationSettings) -> FastAPI:
    _app = FastAPI(
        title=settings.name,
        version=settings.version,
    )
    _app.include_router(router)
    return _app

app = application(get_settings())
