from cortex.contracts.agent import Agent
from cortex.contracts.request import Request
from cortex.contracts.response import Response, ResponseStatus

class EchoAgent(Agent[str,str]):
    """
    An agent that echoes back the input string as the output.
    this is to verify that the agent and the contracts are working as expected.
    """

    def execute(self, request: Request[str]) -> Response[str]:
        return Response(request_id=request.request_id, status=ResponseStatus.SUCCESS, data=request.payload)

    