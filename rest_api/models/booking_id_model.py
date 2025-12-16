from pydantic import BaseModel, Field

class BookingId(BaseModel):
    bookingid: int = Field(alias='bookingId')
