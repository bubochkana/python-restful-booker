import requests
from assertpy import assert_that

from src.clients.booking_client import BookingClient


class TestDeleteBooking:
    def test_delete_booking(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        booking_id = booking_endpoint.create_booking(booking_endpoint.build_random_booking()).json()["bookingid"]
        response = booking_endpoint.delete_booking(booking_id)

        assert_that(response.status_code).is_equal_to(requests.codes.created)

    def test_delete_booking_no_headers(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.delete_booking(booking_endpoint.pick_random_booking_id(), {})
        assert_that(response.status_code).is_equal_to(requests.codes.forbidden)

    def test_delete_booking_no_auth_header(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.delete_booking(
            booking_endpoint.pick_random_booking_id(), headers={"Content-Type": "application/json"}
        )
        assert_that(response.status_code).is_equal_to(requests.codes.forbidden)

    def test_delete_the_same_booking_twice(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        booking_id = booking_endpoint.create_booking(booking_endpoint.build_random_booking()).json()["bookingid"]

        response = booking_endpoint.delete_booking(booking_id)
        # the actual response is 201, probably a defect
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

        response = booking_endpoint.delete_booking(booking_id)
        # the actual response is 405, probably a defect
        (assert_that(response.status_code).is_equal_to(requests.codes.not_found))
