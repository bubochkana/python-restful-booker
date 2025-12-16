from core.utils.common_utils import load_schema
from jsonschema import validate


class TestBookings:
    def test_get_all_booking_ids(self, booking_client):
        response = booking_client.get_booking_ids()
        #TODO - not sure how to assert the status code here as it returns a BookingId object and not the Response object
        # assert response.status_code == 200

    def test_all_booking_ids_schema_validation(self, booking_client):

        response = booking_client.get_booking_ids()
        response.raise_for_status()

        # TODO - not sure how to create the assert here and validate the schema
        # for field in response.json():
        #     validate(instance=field, schema=schema)

    def test_filter_bookings_by_firstname_and_lastname(self, booking_client):
        list_of_bookings = booking_client.get_booking_ids(firstname="John", lastname="Smith")

        assert len(list_of_bookings) > 0


    def test_filter_bookings_by_checkin_and_checkout_dates(self, booking_client):
        list_of_bookings = booking_client.get_booking_ids(checkin="2022-03-13", checkout="2025-05-21")

        assert len(list_of_bookings) > 0

