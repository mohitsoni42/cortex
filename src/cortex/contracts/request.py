from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Generic, Any, TypeVar
from uuid import UUID, uuid4


T = TypeVar("T")

@dataclass(frozen=True)
class Request(Generic[T]):
    """
    Represents an immutable request flowing through the Cortex platform.
    """
    request_id : UUID = field(default_factory=uuid4)
    timestamp : datetime = field(default_factory=lambda: datetime.now(UTC))
    payload : T
    context : dict[str, Any] = field(default_factory=dict)
    