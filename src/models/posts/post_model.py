from pydantic import BaseModel


class BookingDates(BaseModel):
    id: int
    title: str
    body: str
    userId: int
