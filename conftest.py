import pytest
from rest_api.common.booking_client import BookingClient
from rest_api.helpers.booking_helper import BookingHelper


BODY = {
        "firstname": "Anna",
        "lastname": "Voitiuk",
        "totalprice": 120,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-25",
            "checkout": "2026-02-02"
        },
        "additionalneeds": "Bed"
    }


@pytest.fixture
def booking_client():
    return BookingClient()


@pytest.fixture
def booking_helper():
    return BookingHelper()
