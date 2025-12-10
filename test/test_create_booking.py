import pytest


def test_create_booking(booking_client, booking_helper):

    response = booking_client.create_booking(booking_helper.BODY)

    # TODO - Maybe somehow use model in the assert to verify the result?
    assert response.json()['bookingid']
    assert response.json()['booking']['firstname'] == "Anna"
    assert response.json()['booking']['lastname'] == "Voitiuk"
    assert response.json()['booking']['totalprice'] == 120
    assert response.json()['booking']['depositpaid']
    assert response.json()['booking']['bookingdates']['checkin'] == "2025-12-25"
    assert response.json()['booking']['bookingdates']['checkout'] == "2026-02-02"
    assert response.json()['booking']['additionalneeds'] == "Bed"


@pytest.mark.parametrize("case_id, remove, remove_nested", [
    ("missing_firstname", ["firstname"], []),
    ("missing_checkout", [], [("bookingdates", "checkout")]),
    ("missing_totalprice_and_depositpaid", ["totalprice", "depositpaid"], [])
])
def test_create_booking_no_req_fields(case_id, remove, remove_nested,
                                      booking_client, booking_helper):
    body = booking_helper.make_body(remove=remove, remove_nested=remove_nested)

    response = booking_client.create_booking(body)
    assert response.status_code == 500
