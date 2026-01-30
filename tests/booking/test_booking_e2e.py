import pytest
import requests
from assertpy import assert_that

from src.actions.booking_actions import BookingActions
from src.clients.booking.booking_client import BookingClient


class TestBookingE2E:
    @pytest.mark.regression
    def test_booking_create_get_delete_e2e(self):
        actions = BookingActions()

        # create a booking
        created_booking = actions.create_booking()
        booking_id = created_booking.bookingid

        # get created booking
        get_booking_response = actions.get_booking(booking_id)
        actions.assert_comparison_results(created_booking.booking.model_dump(), get_booking_response.model_dump())

        # delete the booking
        actions.delete_booking(booking_id)

        # attempt to get the deleted booking
        #TODO - in case of negative error code, should I call actions or method from he endpoint itself?
        get_booking_response_after_deletion = BookingClient().booking_endpoint().get_booking_by_id(booking_id)
        assert_that(get_booking_response_after_deletion.status_code).is_equal_to(requests.codes.not_found)

    def test_booking_create_update_e2e(self):
        actions = BookingActions()

        # create a booking
        created_booking = actions.create_booking()
        booking_id = created_booking.bookingid

        # get created booking
        get_booking_response = actions.get_booking(booking_id)
        actions.assert_comparison_results(created_booking.booking.model_dump(), get_booking_response.model_dump())

        # update (patch) booking
        updated_booking = actions.update_booking(booking_id)

        # get the booking after update
        get_booking_response = actions.booking_endpoint.get_booking_by_id(booking_id)

        # compare created and updated (patched) bookings
        actions.assert_comparison_results(updated_booking.model_dump(), get_booking_response.json())
