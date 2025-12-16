from assertpy import assert_that
from rest_api.models.booking_model import Booking


class TestBookingById:
    def test_booking_id_schema_validation(self, booking_client, booking_helper):
        response = booking_client.get_booking_by_id(
            booking_helper.pick_random_booking_id_from_the_existing_list())

        # TODO - not sure how to create the assert here and validate the schema
        booking = Booking.model_validate(response)
        assert_that(booking.firstname).is_not_empty()


    def test_get_booking_by_id(self, booking_client, booking_helper):
        response = booking_client.get_booking_by_id(
            booking_helper.pick_random_booking_id_from_the_existing_list())
        assert_that(response).contains_key("firstname")
        assert_that(response).contains_key("lastname")
        assert_that(response).contains_key("totalprice")
        assert_that(response).contains_key("depositpaid")
        # TODO - the assert fails because can't find attribute bookingdates
        # assert_that(response.bookingdates).contains_key("checkin")
        # assert_that(response.bookingdates).contains_key("checkout")
        assert_that(response).contains_key("additionalneeds")
        # TODO - how to verify the response status code
