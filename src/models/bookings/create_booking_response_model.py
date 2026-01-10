from pydantic import BaseModel

from src.models.bookings.booking_id_model import BookingId
from src.models.bookings.booking_model import Booking


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class CreateBookingResponse(BaseModel):
    bookingid: BookingId
    booking: Booking

