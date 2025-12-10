import copy
import random
from rest_api.common.booking_client import BookingClient


class BookingHelper:

    BODY = {
        "firstname": "Anna",
        "lastname": "Voitiuk",
        "totalprice": 120,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-25",
            "checkout": "2026-02-02"
        },
        "additionalneeds": "Bed"
    }

    def make_body(self, remove=None, remove_nested=None):
        body = copy.deepcopy(self.BODY)

        if remove:
            for key in remove:
                body.pop(key, None)

        if remove_nested:
            for parent, child in remove_nested:
                if parent in body and isinstance(body[parent], dict):
                    body[parent].pop(child, None)

        return body

    def create_booking_and_get_id(self):
        return BookingClient().create_booking(self.BODY).json()['bookingid']

    def pick_random_booking_id_from_the_existing_list(self):
        booking_ids_list = BookingClient().get_booking_ids().json()
        return str(random.choice(booking_ids_list)['bookingid'])
