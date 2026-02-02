import pytest
import requests
from assertpy import assert_that

from src.actions.booking_actions import BookingActions
from src.clients.booking.booking_client import BookingClient


class TestCreateBooking:
    @pytest.mark.test_case_id(test_case_id="0007")
    @pytest.mark.parametrize("body", [BookingActions().build_random_booking(),
                                      BookingActions().build_random_booking(),
                                      BookingActions().build_random_booking()],
                             ids=["test_with_body_1", "test_with_body_2", "test_with_body_3"])
    def test_create_booking(self, body):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        actual_result = booking_endpoint.create_booking(body)

        assert_that(actual_result.status_code).is_equal_to(requests.codes.ok)
        BookingActions().assert_comparison_results(body.model_dump(), actual_result.json()["booking"])


    @pytest.mark.parametrize(
        "missed_field",
        [
            pytest.param("firstname", marks=pytest.mark.test_case_id(test_case_id="0008"),
                         id="test_case_id-0008-missed_firstName"),
            pytest.param("lastname", marks=pytest.mark.test_case_id("0009"),
                         id="test_case_id-0009-missed_lastName"),
            pytest.param(
                "totalprice",
                marks=[
                    pytest.mark.test_case_id(test_case_id="0010"),
                    pytest.mark.test_case_id(test_case_id="0011"),
                ],
                id="test_case_id-0010-0011-missed_totalPrice",
            ),
        ],
    )
    def test_create_booking_no_req_fields(self, missed_field):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        body = BookingActions().build_random_booking()
        payload = body.model_dump()
        del payload[missed_field]

        actual_result = booking_endpoint.create_booking(payload)
        # there is a defect in the APIs, the error should be properly handled here
        assert_that(actual_result.status_code).is_equal_to(500)
