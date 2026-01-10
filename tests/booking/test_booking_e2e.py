import requests
from assertpy import assert_that

from src.clients.booking_client import BookingClient
from src.helpers.compare_models import CompareModel


class TestBookingE2E:
    def test_booking_e2e(self):
        # create a booking
        create_request_body = (BookingClient()
                               .get_booking_endpoint()
                               .build_random_booking())
        create_booking_response = (BookingClient()
                                   .get_booking_endpoint()
                                   .create_booking(create_request_body))

        comparison_results = (CompareModel.compare_values(
            create_request_body.model_dump(),
            create_booking_response.json()['booking']))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        booking_id = create_booking_response.json()['bookingid']
        # get the booking
        get_booking_response = (BookingClient()
                                .get_booking_endpoint()
                                .get_booking_by_id(booking_id))

        comparison_results = (CompareModel.compare_values(
            create_request_body.model_dump(),
            get_booking_response.json()))
        assert_that(comparison_results,
                    f"Following differences found: "
                    f"{comparison_results}").is_empty()

        # delete the booking
        BookingClient().get_booking_endpoint().delete_booking(booking_id)

        # get the booking
        get_booking_response_after_deletion = (BookingClient()
                                               .get_booking_endpoint()
                                               .get_booking_by_id(booking_id))
        (assert_that(get_booking_response_after_deletion.status_code)
         .is_equal_to(requests.codes.not_found))
