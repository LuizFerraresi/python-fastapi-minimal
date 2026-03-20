from enum import StrEnum


class HealthStatus(StrEnum):
    OK = "ok"
    READY = "ready"
    NOT_READY = "not-ready"
