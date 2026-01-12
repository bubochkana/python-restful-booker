from assertpy import assert_that
import requests

from src.clients.booking_client import BookingClient
from src.models.bookings.booking_model import BookingModel


class TestBookingById:
    def test_booking_schema_validation(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.get_booking_by_id(
            booking_endpoint.pick_random_booking_id())

        BookingModel.model_validate(response.json())

    def test_get_booking_by_id(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.get_booking_by_id(
            booking_endpoint.pick_random_booking_id())
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

        assert_that(response.json()).contains_key("firstname")
        assert_that(response.json()).contains_key("lastname")
        assert_that(response.json()).contains_key("totalprice")
        assert_that(response.json()).contains_key("depositpaid")
        assert_that(response.json()['bookingdates']).contains_key("checkin")
        assert_that(response.json()['bookingdates']).contains_key("checkout")
        assert_that(response.json()).contains_key("additionalneeds")
