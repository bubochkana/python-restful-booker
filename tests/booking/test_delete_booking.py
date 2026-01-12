import requests
from assertpy import assert_that

from src.clients.booking_client import BookingClient


class TestDeleteBooking:
    def test_delete_booking(self):
        booking_id = BookingClient().get_booking_endpoint().create_booking(
            BookingClient().get_booking_endpoint()
            .build_random_booking()).json()['bookingid']
        response = (BookingClient().get_booking_endpoint()
                    .delete_booking(booking_id))

        assert_that(response.status_code).is_equal_to(requests.codes.created)

    def test_delete_booking_no_headers(self):
        response = BookingClient().get_booking_endpoint().delete_booking(
            BookingClient().get_booking_endpoint()
            .pick_random_booking_id(), {})
        assert_that(response.status_code).is_equal_to(requests.codes.forbidden)

    def test_delete_booking_no_auth_header(self):
        response = BookingClient().get_booking_endpoint().delete_booking(
            BookingClient().get_booking_endpoint()
            .pick_random_booking_id(),
            headers={"Content-Type": "application/json"})
        assert_that(response.status_code).is_equal_to(requests.codes.forbidden)

    def test_delete_the_same_booking_twice(self):
        booking_id = BookingClient().get_booking_endpoint().create_booking(
            BookingClient().get_booking_endpoint()
            .build_random_booking()).json()['bookingid']

        response = (BookingClient().get_booking_endpoint()
                    .delete_booking(booking_id))
        assert_that(response.status_code).is_equal_to(requests.codes.created)

        response = (BookingClient().get_booking_endpoint()
                    .delete_booking(booking_id))
        (assert_that(response.status_code)
         .is_equal_to(requests.codes.method_not_allowed))
