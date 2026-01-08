import random
from typing import Optional
import requests
from faker import Faker

from src.clients.booking_client import BookingClient
from src.models.bookings.booking_id_model import BookingId
from src.models.bookings.booking_model import Booking
from src.models.bookings.create_booking_response_model import BookingDates


class BookingEndpoint:
    def __init__(self, host: str):
        self.host = host

    def get_all_bookings(
        self,
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
        checkin: Optional[str] = None,
        checkout: Optional[str] = None,
    ):
        params = {
            "firstname": firstname,
            "lastname": lastname,
            "checkin": checkin,
            "checkout": checkout}

        params = {key: value for key, value in params.items()
                  if value is not None}

        return requests.get(f"{self.host}/booking", params=params)

    def get_booking_by_id(self, booking_id):
        return requests.get(f"{self.host}/booking/{booking_id}")

    def create_booking(self, body: Booking):
        return requests.post(
            f"{self.host}/booking", json=body.model_dump())

    def update_booking(self, booking_id, body, headers=None):
        token = BookingClient().get_auth_endpoint().get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.put(
            f"{self.host}/booking/{booking_id}",
            json=body.model_dump(),
            headers=final_headers).json()

    def delete_booking(self, booking_id, headers=None):
        token = BookingClient().get_auth_endpoint().get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.delete(
            f"{self.host}/booking/{booking_id}", headers=final_headers)

    def build_random_booking(self) -> Booking:
        faker: Faker = Faker()
        return Booking(firstName=faker.first_name(),
                       lastName=faker.last_name(),
                       totalPrice=faker.random_int(min=1, max=500),
                       depositPaid=faker.boolean(),
                       bookingDates=BookingDates(
                           checkIn=faker.date(pattern="%Y-%m-%d"),
                           checkOut=faker.date(pattern="%Y-%m-%d")),
                       additionalNeeds=faker.name())

    def pick_random_booking_id_from_the_existing_list(self) -> str:
        booking_ids_list = (self.get_all_bookings())
        my_obj_list: list[BookingId] = [BookingId(**dict_item)
                                        for dict_item
                                        in booking_ids_list.json()]
        return str(random.choice(my_obj_list).bookingid)
