
class TestUpdateBooking:
    def test_update_booking(self, booking_client):

        booking_id_to_update \
            = booking_client.pick_random_booking_id_from_the_existing_list()

        updated_booking = booking_client.update_booking(
            booking_id_to_update, booking_client.build_random_booking())

        # TODO - not sure how to use the model in the assert to verify the result?

    def test_update_booking_no_auth_header(self, booking_client):
        booking_id_to_update \
            = booking_client.pick_random_booking_id_from_the_existing_list()
        response = booking_client.update_booking(
            booking_id_to_update, booking_client.build_random_booking(),
            headers={"Content-Type": "application/json",
                     "Accept": "application/json"})
        # TODO - not sure how to use the assert to verify the response code 403
        # assert response.status_code == 403
