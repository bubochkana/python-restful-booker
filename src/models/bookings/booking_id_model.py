from pydantic import BaseModel


class BookingIdModel(BaseModel):
    bookingid: int
