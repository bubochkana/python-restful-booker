from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BookingDates(BaseModel):
    checkin: str = Field(alias='checkIn')
    checkout: str = Field(alias='checkOut')


class Booking(BaseModel):
    firstname: str = Field(alias='firstName')
    lastname: str = Field(alias='lastName')
    totalprice: int = Field(alias='totalPrice')
    depositpaid: bool = Field(alias='depositPaid')
    bookingdates: BookingDates = Field(alias='bookingDates')
    additionalneeds: Optional[str] = Field(alias='additionalNeeds', default=None)
