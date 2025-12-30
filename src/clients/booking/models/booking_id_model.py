from pydantic import BaseModel


class BookingId(BaseModel):
    bookingid: int
