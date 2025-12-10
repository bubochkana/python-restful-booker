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
