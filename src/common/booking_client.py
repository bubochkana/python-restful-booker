from typing import Optional

import requests
from src.utils.booker_config_parser import ConfigurationParser
from src.common.auth_client import AuthClient
from src.models.booking_model import Booking


class BookingClient:
    def __init__(self):
        self.host = ConfigurationParser().get_restful_booker_api_url()

    def get_booking_ids(self,
                        firstname: Optional[str] = None,
                        lastname: Optional[str] = None,
                        checkin: Optional[str] = None,
                        checkout: Optional[str] = None):
        params = {
            "firstname": firstname,
            "lastname": lastname,
            "checkin": checkin,
            "checkout": checkout
        }

        params = {key: value for key, value in params.items() if value is not None}

        return requests.get(f"{self.host}/booking", params=params)

    def get_booking_by_id(self, booking_id):
        return requests.get(f"{self.host}/booking/{booking_id}")

    def create_booking(self, body: Booking):
        return requests.post(f"{self.host}/booking", json=body.model_dump())

    def update_booking(self, booking_id, body, headers=None):
        token = AuthClient().get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.put(f"{self.host}/booking/{booking_id}",
                            json=body.model_dump(),
                            headers=final_headers).json()

    def delete_booking(self, booking_id, headers=None):
        token = AuthClient().get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.delete(f"{self.host}/booking/{booking_id}",
                               headers=final_headers)
