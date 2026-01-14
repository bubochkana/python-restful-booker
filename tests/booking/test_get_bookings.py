import requests
from assertpy import assert_that
from faker import Faker

from src.clients.booking_client import BookingClient
from src.models.bookings.booking_id_model import BookingIdModel


class TestBookings:
    def test_get_all_booking_ids(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.get_all_bookings()
        assert_that(response.status_code).is_equal_to(requests.codes.ok)

    def test_all_bookings_schema_validation(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.get_all_bookings()
        for booking_id in response.json():
            BookingIdModel.model_validate(booking_id)

    def test_filter_bookings_by_firstname_and_lastname(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        response = booking_endpoint.get_all_bookings(
            firstName="John", lastName="Smith")
        assert_that(response.json()).is_not_empty()

    def generate_checkin_checkout_dates(self):
        faker = Faker()
        checkin_date = faker.date_between(
            start_date = "-7y",
            end_date = "today"
        )

        checkout_date = faker.date_between(
            start_date = checkin_date,
            end_date = "+1y"
        )

        checkin = checkin_date.strftime("%Y-%m-%d")
        checkout = checkout_date.strftime("%Y-%m-%d")

        return checkin, checkout

    def test_filter_bookings_by_checkin_and_checkout_dates(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        checkin, checkout = self.generate_checkin_checkout_dates()

        response = booking_endpoint.get_all_bookings(
            checkin=checkin,
            checkout=checkout)
        assert_that(response.json()).is_not_empty()
