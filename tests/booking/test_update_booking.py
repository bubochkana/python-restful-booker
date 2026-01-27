import requests
from assertpy import assert_that

from src.actions.booking_actions import BookingActions
from src.clients.booking.booking_client import BookingClient
from src.helpers.compare_models import CompareModel


class TestUpdateBooking:
    def test_update_booking(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        booking_id_to_update = BookingActions().pick_random_booking_id()

        random_booking = BookingActions().build_random_booking()
        updated_booking = booking_endpoint.update_booking(booking_id_to_update, random_booking)

        comparison_results = CompareModel().compare_values(random_booking.model_dump(), updated_booking.json())
        BookingActions().assert_comparison_results(comparison_results)

    def test_update_booking_no_auth_header(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        booking_id_to_update = BookingActions().pick_random_booking_id()
        response = (booking_endpoint.update_booking(booking_id_to_update,
                BookingActions().build_random_booking(),
                headers={"Content-Type": "application/json", "Accept": "application/json"},
            )
        )
        assert_that(response.status_code).is_equal_to(requests.codes.forbidden)
