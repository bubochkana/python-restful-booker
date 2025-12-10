import requests
from core.utils.booker_config_parser import get_booking_ids_api_url
from rest_api.common.auth_client import AuthClient


class BookingClient:
    BOOKING_URL = get_booking_ids_api_url()

    def get_booking_ids(self,
                        firstname=None,
                        lastname=None,
                        checkin=None,
                        checkout=None):
        params = {
            "firstname": firstname,
            "lastname": lastname,
            "checkin": checkin,
            "checkout": checkout
        }

        params = {key: value for key, value in params.items() if value is not None}

        return requests.get(self.BOOKING_URL, params=params)

    def get_booking_by_id(self, booking_id):
        return requests.get(self.BOOKING_URL + booking_id)

    def create_booking(self, body):
        return requests.post(self.BOOKING_URL, json=body)

    def delete_booking(self, booking_id, headers=None):
        token = AuthClient().get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.delete(self.BOOKING_URL + str(booking_id),
                               headers=final_headers)
