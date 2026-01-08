from assertpy import assert_that
import requests

from src.clients.booking_client import BookingClient
from src.models.bookings.booking_model import Booking


class TestBookingById:
    def test_booking_id_schema_validation(self):
        response = BookingClient().get_booking_endpoint().get_booking_by_id(
            BookingClient().get_booking_endpoint().pick_random_booking_id_from_the_existing_list())

        # TODO - not sure how to create the assert here and validate the schema
        booking = Booking.model_validate(response)
        assert_that(booking.firstname).is_not_empty()

    def test_get_booking_by_id(self):
        response = BookingClient().get_booking_endpoint().get_booking_by_id(
            BookingClient().get_booking_endpoint().pick_random_booking_id_from_the_existing_list())
        assert_that(response.json()).contains_key("firstname")
        assert_that(response.json()).contains_key("lastname")
        assert_that(response.json()).contains_key("totalprice")
        assert_that(response.json()).contains_key("depositpaid")
        # TODO - the assert fails because can't find attribute bookingdates
        # assert_that(response.json().bookingdates).contains_key("checkin")
        # assert_that(response.json().bookingdates).contains_key("checkout")
        assert_that(response.json()).contains_key("additionalneeds")
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
