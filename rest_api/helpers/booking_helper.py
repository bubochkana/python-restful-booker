import copy
import random
from typing import Optional, Iterable, Tuple

from rest_api.common.booking_client import BookingClient
from rest_api.models.booking_model import Booking
from rest_api.models.booking_model import BookingDates



class BookingHelper:

    BODY = Booking(firstName="Anna",
                   lastName="Voitiuk",
                   totalPrice=120,
                   depositPaid=True,
                   bookingDates=BookingDates(
                       checkIn="2025-12-25",
                       checkOut="2026-02-02"),
                   additionalNeeds="Bed")

    def make_body(self, remove: Optional[Iterable[str]] = None,
                  remove_nested: Optional[Iterable[Tuple[str,str]]] = None) -> Booking:
        body_dict = copy.deepcopy(self.BODY).model_dump()

        if remove:
            for key in remove:
                body_dict.pop(key, None)

        if remove_nested:
            for parent, child in remove_nested:
                if parent in body_dict and isinstance(body_dict[parent], dict):
                    body_dict[parent].pop(child, None)

        return Booking.model_validate(body_dict)

    def create_booking_and_get_id(self) -> int:
        return BookingClient().create_booking(self.BODY)['bookingid']

    def pick_random_booking_id_from_the_existing_list(self) -> str:
        booking_ids_list = BookingClient().get_booking_ids()
        return str(random.choice(booking_ids_list)['bookingid'])
