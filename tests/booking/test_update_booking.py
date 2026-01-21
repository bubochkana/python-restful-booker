import requests
from assertpy import assert_that

from src.clients.booking.booking_client import BookingClient
from src.helpers.compare_models import CompareModel


class TestUpdateBooking:
    def test_update_booking(self):
        booking_id_to_update = BookingClient().booking_endpoint().pick_random_booking_id()

        random_booking = BookingClient().booking_endpoint().build_random_booking()
        updated_booking = BookingClient().booking_endpoint().update_booking(booking_id_to_update, random_booking)

        comparison_results = CompareModel.compare_values(random_booking.model_dump(), updated_booking.json())
        assert_that(comparison_results, f"Following differences found: {comparison_results}").is_empty()

    def test_update_booking_no_auth_header(self):
        booking_id_to_update = BookingClient().booking_endpoint().pick_random_booking_id()
        response = (
            BookingClient()
            .booking_endpoint()
            .update_booking(
                booking_id_to_update,
                BookingClient().booking_endpoint().build_random_booking(),
                headers={"Content-Type": "application/json", "Accept": "application/json"},
            )
        )
        assert_that(response.status_code).is_equal_to(requests.codes.forbidden)
