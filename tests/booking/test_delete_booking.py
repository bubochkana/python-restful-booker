from src.clients.booking_client import BookingClient


class TestDeleteBooking:
    def test_delete_booking(self):
        booking_id = BookingClient().get_booking_endpoint().create_booking(
            BookingClient().get_booking_endpoint().build_random_booking()).json()['bookingid']
        response = BookingClient().get_booking_endpoint().delete_booking(booking_id)
        assert response.status_code == 201

    def test_delete_booking_no_headers(self):
        response = BookingClient().get_booking_endpoint().delete_booking(
            BookingClient().get_booking_endpoint().pick_random_booking_id_from_the_existing_list(), {})
        assert response.status_code == 403

    def test_delete_booking_no_auth_header(self):
        response = BookingClient().get_booking_endpoint().delete_booking(
            BookingClient().get_booking_endpoint().pick_random_booking_id_from_the_existing_list(),
            headers={"Content-Type": "application/json"})
        assert response.status_code == 403

    def test_delete_the_same_booking_twice(self):
        booking_id = BookingClient().get_booking_endpoint().create_booking(
            BookingClient().get_booking_endpoint().build_random_booking()).json()['bookingid']

        response = BookingClient().get_booking_endpoint().delete_booking(booking_id)
        assert response.status_code == 201

        response = BookingClient().get_booking_endpoint().delete_booking(booking_id)
        assert response.status_code == 405
