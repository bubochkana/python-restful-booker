def test_create_booking(booking_client, booking_helper):

    booking_id_to_update = booking_helper.pick_random_booking_id_from_the_existing_list()

    response = booking_client.update_booking(booking_id_to_update, booking_helper.BODY)

    # TODO - Maybe somehow use model in the assert to verify the result?
    assert response.json()['firstname'] == "Anna"
    assert response.json()['lastname'] == "Voitiuk"
    assert response.json()['totalprice'] == 120
    assert response.json()['depositpaid']
    assert response.json()['bookingdates']['checkin'] == "2025-12-25"
    assert response.json()['bookingdates']['checkout'] == "2026-02-02"
    assert response.json()['additionalneeds'] == "Bed"


def test_update_booking_no_auth_header(booking_client, booking_helper):
    booking_id_to_update = booking_helper.pick_random_booking_id_from_the_existing_list()
    response = booking_client.update_booking(booking_id_to_update, booking_helper.BODY,
                                             headers={"Content-Type": "application/json",
                                                      "Accept": "application/json"})
    assert response.status_code == 403
