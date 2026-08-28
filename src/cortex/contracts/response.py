from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Any, Generic, TypeVar
from uuid import UUID, uuid4


T = TypeVar("T")


class ResponseStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"


@dataclass(frozen=True, kw_only=True)
class Response(Generic[T]):
    """
    Represents an immutable response produced during Cortex execution.
    """

    response_id: UUID = field(default_factory=uuid4)
    request_id: UUID
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    status: ResponseStatus
    data: T | None = None
    error: str | None = None