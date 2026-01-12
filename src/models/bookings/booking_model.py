from typing import Optional

from pydantic import BaseModel


class BookingDatesModel(BaseModel):
    checkin: str
    checkout: str


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDatesModel
    additionalneeds: Optional[str]
