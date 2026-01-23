import requests
from assertpy import assert_that

from src.actions.booking_actions import BookingActions
from src.clients.booking.booking_client import BookingClient
from src.models.bookings.booking_model import BookingModel


class TestBookingById:
    def test_booking_schema_validation(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        # TODO - I moved pick_random_booking_id() method to the BookingActions class, so how to properly use the method in this test now?
        response = booking_endpoint.get_booking_by_id(BookingActions().pick_random_booking_id())

        BookingModel.model_validate(response.json())

    def test_get_booking_by_id(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.get_booking_by_id(BookingActions().pick_random_booking_id())
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

        booking_model = BookingModel.model_validate(response.json()).model_dump()
        assert_that(booking_model).contains_key("firstname")
        assert_that(booking_model).contains_key("lastname")
        assert_that(booking_model).contains_key("totalprice")
        assert_that(booking_model).contains_key("depositpaid")
        assert_that(booking_model["bookingdates"]).contains_key("checkin")
        assert_that(booking_model["bookingdates"]).contains_key("checkout")
        assert_that(booking_model).contains_key("additionalneeds")
