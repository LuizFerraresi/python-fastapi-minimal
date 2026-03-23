from .interfaces import ApplicationSettings


async def index(settings: ApplicationSettings) -> dict[str, str]:
    return {
        "name": settings.name,
        "version": settings.version
    }
