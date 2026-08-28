from cortex.agents.echo import EchoAgent  # type: ignore
from cortex.contracts.request import Request  # type: ignore
from cortex.contracts.response import ResponseStatus  # type: ignore


class TestEchoAgent:
    def test_echo_returns_payload(self):
        agent = EchoAgent()
        request = Request[str](payload="Hello Cortex!")
        response = agent.execute(request)
        assert response.data == "Hello Cortex!"

    def test_echo_preserves_request_id(self):
        agent = EchoAgent()
        request = Request[str](payload="Hello someone!")
        response = agent.execute(request)
        assert response.request_id == request.request_id

    def test_echo_response_status_success(self):
        agent = EchoAgent()
        request = Request[str](payload="Hello Cortex!")
        response = agent.execute(request)
        assert response.status == ResponseStatus.SUCCESS