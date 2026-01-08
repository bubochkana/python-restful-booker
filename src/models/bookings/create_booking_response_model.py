from datetime import datetime

from pydantic import BaseModel, Field

from src.models.bookings.booking_id_model import BookingId
from src.models.bookings.booking_model import Booking


class BookingDates(BaseModel):
    checkin: str = Field(alias="checkIn")
    checkout: str = Field(alias="checkOut")


class CreateBookingResponse(BaseModel):
    bookingid: BookingId = Field(alias="bookingId")
    booking: Booking
