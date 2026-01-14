import requests
from assertpy import assert_that

from src.clients.booking_client import BookingClient
from src.helpers.compare_models import CompareModel
from src.models.bookings.booking_model import BookingModel, \
    CreateBookingResponse


class TestBookingE2E:
    def test_booking_create_get_delete_e2e(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        # create a booking
        create_request_body = booking_endpoint.build_random_booking()
        create_booking_response = (booking_endpoint.create_booking(
            create_request_body))
        booking_model = CreateBookingResponse(**create_booking_response.json())

        comparison_results = (CompareModel().compare_values(
            create_request_body.model_dump(),
            booking_model.booking.model_dump()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        booking_id = booking_model.bookingid

        # get the booking
        get_booking_response = (booking_endpoint
                                .get_booking_by_id(booking_id))
        comparison_results = (CompareModel().compare_values(
            create_request_body.model_dump(),
            get_booking_response.json()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        # delete the booking
        booking_endpoint.delete_booking(booking_id)

        # get the booking
        get_booking_response_after_deletion = booking_endpoint.get_booking_by_id(booking_id)
        assert_that(get_booking_response_after_deletion.status_code).is_equal_to(requests.codes.not_found)

    def test_booking_create_update_e2e(self):
        client = BookingClient()
        booking_endpoint = client.booking_endpoint()

        # create a booking
        create_request_body = booking_endpoint.build_random_booking()
        create_booking_response = booking_endpoint.create_booking(create_request_body)
        booking_model = CreateBookingResponse(**create_booking_response.json())

        comparison_results = (CompareModel().compare_values(
            create_request_body.model_dump(),
            booking_model.booking.model_dump()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        booking_id = booking_model.bookingid

        # get the booking after create
        get_booking_response = (booking_endpoint.get_booking_by_id(booking_id))
        comparison_results = (CompareModel().compare_values(
            create_request_body.model_dump(),
            get_booking_response.json()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        # update (patch) booking
        update_request_body = booking_endpoint.build_random_booking()
        update_booking_response = booking_endpoint.update_booking(booking_id, update_request_body)
        update_booking_model = BookingModel(**update_booking_response.json())

        comparison_results = (CompareModel().compare_values(
            update_request_body.model_dump(),
            update_booking_model.model_dump()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        # get the booking after update
        get_booking_response = (booking_endpoint
                                .get_booking_by_id(booking_id))

       # compare created and updated (patched) bookings
        comparison_results = (CompareModel().compare_values(
            update_request_body.model_dump(),
            get_booking_response.json()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()



