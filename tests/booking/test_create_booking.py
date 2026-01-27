import requests
from assertpy import assert_that

from src.actions.booking_actions import BookingActions
from src.clients.booking.booking_client import BookingClient
from src.helpers.compare_models import CompareModel


class TestCreateBooking:
    def test_create_booking(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        body = BookingActions().build_random_booking()
        actual_result = booking_endpoint.create_booking(body)

        assert_that(actual_result.status_code).is_equal_to(requests.codes.ok)
        BookingActions().assert_comparison_results(body.model_dump(), actual_result.json()["booking"])

    # TODO - find a way to write a test when one of the required fields is missing
    # @pytest.mark.parametrize("case_id, remove, remove_nested", [
    #     ("missing_firstname", ["firstName"], []),
    #     ("missing_checkout", [], [("bookingDates", "checkOut")]),
    #     ("missing_totalprice_and_depositpaid", ["totalPrice", "depositPaid"], [])
    # ])
    # def test_create_booking_no_req_fields(self, case_id, remove, remove_nested,
    #                                       booking_client, booking_client):
    #     body = booking_client.make_body(remove=remove, remove_nested=remove_nested)
    #
    #     response = booking_client.create_booking(body)
    #     assert response.status_code == 500
