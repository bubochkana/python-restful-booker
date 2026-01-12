import requests
from assertpy import assert_that

from src.clients.booking_client import BookingClient
from src.models.bookings.booking_id_model import BookingIdModel


class TestBookings:
    def test_get_all_booking_ids(self):
        response = BookingClient().get_booking_endpoint().get_all_bookings()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

    def test_all_bookings_schema_validation(self):
        response = BookingClient().get_booking_endpoint().get_all_bookings()
        for booking_id in response.json():
            BookingIdModel.model_validate(booking_id)

    def test_filter_bookings_by_firstname_and_lastname(self):
        response = BookingClient().get_booking_endpoint().get_all_bookings(
            firstname="John", lastname="Smith")
        assert_that(response.json()).is_not_empty()

    def test_filter_bookings_by_checkin_and_checkout_dates(self):
        response = BookingClient().get_booking_endpoint().get_all_bookings(
            checkin="2018-01-01",
            checkout="2019-01-01")
        assert_that(response.json()).is_not_empty()
