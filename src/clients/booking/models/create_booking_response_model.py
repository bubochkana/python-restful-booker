from datetime import datetime

from pydantic import BaseModel, Field

from src.clients.booking.models.booking_id_model import BookingId
from src.clients.booking.models.booking_model import Booking


class BookingDates(BaseModel):
    checkin: datetime = Field(alias="checkIn")
    checkout: datetime = Field(alias="checkOut")


class CreateBookingResponse(BaseModel):
    bookingid: BookingId = Field(alias="bookingId")
    booking: Booking
