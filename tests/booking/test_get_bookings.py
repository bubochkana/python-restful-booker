import requests
from assertpy import assert_that

from src.models.bookings.booking_id_model import BookingId


class TestBookings:
    def test_get_all_booking_ids(self, booking_client):
        response = booking_client.get_booking_endpoint().get_all_bookings()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

    def test_all_booking_ids_schema_validation(self, booking_client):

        response = booking_client.get_all_bookings()

        # TODO - not sure how to create the assert here and validate the schema
        BookingId.model_validate_json(json_data=response.json())

    def test_filter_bookings_by_firstname_and_lastname(self, booking_client):
        response = booking_client.get_all_bookings(
            firstname="John", lastname="Smith")
        assert_that(response.json()).is_not_empty()

    def test_filter_bookings_by_checkin_and_checkout_dates(
            self, booking_client):
        response = booking_client.get_all_bookings(
            checkin="2018-01-01",
            checkout="2019-01-01")
        assert_that(response.json()).is_not_empty()
