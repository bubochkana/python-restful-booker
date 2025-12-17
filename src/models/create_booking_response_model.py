from pydantic import BaseModel, Field
from datetime import datetime
from src.models.booking_model import Booking
from src.models.booking_id_model import BookingId


class BookingDates(BaseModel):
    checkin: datetime = Field(alias='checkIn')
    checkout: datetime = Field(alias='checkOut')


class CreateBookingResponse(BaseModel):
    bookingid: BookingId = Field(alias='bookingId')
    booking: Booking
