import pytest
from src.common.booking_client import BookingClient
from src.helpers.booking_helper import BookingHelper

@pytest.fixture
def booking_client():
    return BookingClient()


@pytest.fixture
def booking_helper():
    return BookingHelper()
