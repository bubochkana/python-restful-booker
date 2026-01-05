import random
from src.clients.booking.booking_client import BookingClient
from src.models.bookings.booking_id_model import BookingId
from src.models.bookings.booking_model import Booking, BookingDates
from faker import Faker


class BookingHelper:

    @staticmethod
    def build_random_booking() -> Booking:
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
        booking_ids_list = BookingClient().get_all_bookings()
        my_obj_list: list[BookingId] = [BookingId(**dict_item) for dict_item in booking_ids_list.json()]
        return str(random.choice(my_obj_list).bookingid)
