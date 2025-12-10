from core.utils.common_utils import load_schema
from jsonschema import validate


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
