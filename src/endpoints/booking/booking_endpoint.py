import random
import requests
from faker import Faker
from requests import Response

from src.models.bookings.booking_model import BookingModel, BookingDatesModel, \
    BookingIdModel


class BookingEndpoint:
    def __init__(self, host: str, auth_endpoint=None):
        self.host = host
        self.auth_endpoint = auth_endpoint

    def get_all_bookings(
        self,
        firstname: str = None,
        lastname: str = None,
        checkin: str = None,
        checkout: str = None,
    ) -> Response:
        params = {
            "firstname": firstname,
            "lastname": lastname,
            "checkin": checkin,
            "checkout": checkout}

        params = {key: value for key, value in params.items()
                  if value is not None}

        return requests.get(f"{self.host}/booking", params=params)

    def get_booking_by_id(self, booking_id) -> Response:
        return requests.get(f"{self.host}/booking/{booking_id}")

    def create_booking(self, body: BookingModel) -> Response:
        return requests.post(
            f"{self.host}/booking", json=body.model_dump())

    def update_booking(self, booking_id, body, headers = None) -> Response:
        token = self.auth_endpoint.get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.put(
            f"{self.host}/booking/{booking_id}",
            json=body.model_dump(),
            headers=final_headers)

    def delete_booking(self, booking_id, headers = None) -> Response:
        token = self.auth_endpoint.get_token()
        default_headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }

        final_headers = default_headers if headers is None else headers

        return requests.delete(
            f"{self.host}/booking/{booking_id}", headers = final_headers)

    def build_random_booking(self) -> BookingModel:
        faker: Faker = Faker()
        return BookingModel(firstname=faker.first_name(),
                            lastname=faker.last_name(),
                            totalprice=faker.random_int(min=1, max=500),
                            depositpaid=faker.boolean(),
                            bookingdates=BookingDatesModel(
                                checkin=faker.date(pattern="%Y-%m-%d"),
                                checkout=faker.date(pattern="%Y-%m-%d")),
                            additionalneeds=faker.name())

    def pick_random_booking_id(self) -> str:
        booking_ids_list = (self.get_all_bookings())
        my_obj_list: list[BookingIdModel] = [BookingIdModel(**dict_item)
                                             for dict_item
                                             in booking_ids_list.json()]
        return str(random.choice(my_obj_list).bookingid)
