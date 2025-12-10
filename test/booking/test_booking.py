import pytest

from core.utils.common_utils import load_schema
from jsonschema import validate


def test_get_all_booking_ids(booking_client):
    response = booking_client.get_booking_ids()
    assert response.status_code == 200


def test_all_booking_ids_schema_validation(booking_client):
    schema = load_schema('get_all_booking_ids_json_schema.json')

    response = booking_client.get_booking_ids()
    response.raise_for_status()

    for field in response.json():
        validate(instance=field, schema=schema)


def test_filter_bookings_by_firstname_and_lastname(booking_client):
    response = booking_client.get_booking_ids(firstname="John", lastname="Smith")

    assert len(response.json()) > 0
    response.raise_for_status()


def test_filter_bookings_by_checkin_and_checkout_dates(booking_client):
    response = booking_client.get_booking_ids(checkin="2022-03-13", checkout="2025-05-21")

    assert len(response.json()) > 0
    response.raise_for_status()


def test_booking_id_schema_validation(booking_client, booking_helper):
    schema = load_schema('get_booking_id_json_schema.json')

    response = booking_client.get_booking_by_id(
        booking_helper.pick_random_booking_id_from_the_existing_list())
    response.raise_for_status()

    for field in response.json():
        validate(instance=field, schema=schema)


def test_get_booking_by_id(booking_client, booking_helper):
    response = booking_client.get_booking_by_id(
        booking_helper.pick_random_booking_id_from_the_existing_list())
    assert response.status_code == 200


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
