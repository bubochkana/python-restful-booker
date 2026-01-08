from src.clients.booking_client import BookingClient


class TestUpdateBooking:
    def test_update_booking(self):

        booking_id_to_update \
            = BookingClient().get_booking_endpoint().pick_random_booking_id_from_the_existing_list()

        updated_booking = BookingClient().get_booking_endpoint().update_booking(
            booking_id_to_update, BookingClient().get_booking_endpoint().build_random_booking())

        # TODO - not sure how to use the model in the assert to verify the result?

    def test_update_booking_no_auth_header(self):
        booking_id_to_update \
            = BookingClient().get_booking_endpoint().pick_random_booking_id_from_the_existing_list()
        response = BookingClient().get_booking_endpoint().update_booking(
            booking_id_to_update, BookingClient().get_booking_endpoint().build_random_booking(),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"})
        # TODO - not sure how to use the assert to verify the response code 403
        # assert response.status_code == 403
