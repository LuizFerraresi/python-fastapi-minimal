
from .interfaces import Repository
from .constants import HealthStatus


class HealthcheckService:

    @staticmethod
    def ping() -> HealthStatus:
        return HealthStatus.OK

    def __init__(self, **repositories: Repository) -> None:
        self._repositories = repositories
    
    async def readiness(self) -> HealthStatus:
        # status = [await repository.ping() for repository in self._repositories.values()]
        status = [True, True, True]
        return HealthStatus.READY if all(status) else HealthStatus.NOT_READY
