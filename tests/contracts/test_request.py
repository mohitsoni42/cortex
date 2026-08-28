from uuid import UUID
from datetime import datetime, timezone
import pytest
from dataclasses import FrozenInstanceError
from cortex.contracts.request import Request


class TestRequest:

    def test_request_is_immutable(self):
        request = Request[str](payload="Hello Cortex!")
        with pytest.raises(FrozenInstanceError):
            request.payload = "New Payload"
        
    def test_request_has_uuid(self):
        request = Request[str](payload="Hello Cortex!")
        assert isinstance(request.request_id, UUID)

    def test_request_has_utc_timestamp(self):
        request = Request[str](payload="Hello Cortex!")
        assert request.timestamp.tzinfo == timezone.utc

    def test_different_requests_have_different_uuids(self):
        request1 = Request[str](payload="Hello Cortex!")
        request2 = Request[str](payload="Hello Cortex!")
        assert request1.request_id != request2.request_id

    def test_requests_have_independent_context(self):
        request1 = Request[str](payload="Request 1")
        request2 = Request[str](payload="Request 2")

        request1.context["key"] = "value"

        assert "key" not in request2.context

