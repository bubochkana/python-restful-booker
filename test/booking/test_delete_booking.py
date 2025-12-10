def test_delete_booking(booking_client, booking_helper):
    booking_id = booking_client.create_booking(booking_helper.BODY).json()['bookingid']
    response = booking_client.delete_booking(booking_id)
    assert response.status_code == 201


def test_delete_booking_no_headers(booking_client, booking_helper):
    response = booking_client.delete_booking(
        booking_helper.pick_random_booking_id_from_the_existing_list(), {})
    assert response.status_code == 403


def test_delete_booking_no_auth_header(booking_client, booking_helper):
    response = booking_client.delete_booking(
        booking_helper.pick_random_booking_id_from_the_existing_list(),
        headers={"Content-Type": "application/json"})
    assert response.status_code == 403


def test_delete_the_same_booking_twice(booking_client, booking_helper):
    booking_id = booking_client.create_booking(booking_helper.BODY).json()['bookingid']

    response = booking_client.delete_booking(booking_id)
    assert response.status_code == 201

    response = booking_client.delete_booking(booking_id)
    assert response.status_code == 405
