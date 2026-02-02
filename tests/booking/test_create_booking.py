import pytest
import requests
from assertpy import assert_that

from src.actions.booking_actions import BookingActions
from src.clients.booking.booking_client import BookingClient


class TestCreateBooking:
    @pytest.mark.parametrize("body", [BookingActions().build_random_booking(),
                                      BookingActions().build_random_booking(),
                                      BookingActions().build_random_booking()])
    def test_create_booking(self, body):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        actual_result = booking_endpoint.create_booking(body)

        assert_that(actual_result.status_code).is_equal_to(requests.codes.ok)
        BookingActions().assert_comparison_results(body.model_dump(), actual_result.json()["booking"])

    @pytest.mark.parametrize("missed_field", ["firstName", "totalPrice"])
    def test_create_booking_no_req_fields(self, missed_field):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        body = BookingActions().build_random_booking()
        payload = body.model_dump(by_alias=True)
        del payload[missed_field]

        actual_result = booking_endpoint.create_booking(payload)
        # there is a defect in the APIs, the error should be properly handled here
        assert_that(actual_result.status_code).is_equal_to(500)
