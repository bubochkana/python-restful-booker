from pydantic import BaseModel

from src.models.bookings.booking_id_model import BookingIdModel
from src.models.bookings.booking_model import BookingModel


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class CreateBookingResponse(BaseModel):
    bookingid: BookingIdModel
    booking: BookingModel

