from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from cortex.contracts.request import Request
from cortex.contracts.response import Response

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class Agent(ABC, Generic[InputT, OutputT]):
    """
    Base contract for every Cortex agent.

    An Agent transforms a Request into a Response by performing a
    single domain-specific responsibility.
    """

    @abstractmethod
    def execute(
        self,
        request: Request[InputT],
    ) -> Response[OutputT]:
        """
        Execute the agent's responsibility.

        Implementations should either return a valid Response or raise
        an exception when execution cannot be completed.
        """
        raise NotImplementedError