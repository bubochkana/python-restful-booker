from pydantic import BaseModel, ConfigDict, Field


class BookingDatesModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    checkin: str = Field(alias = "checkIn")
    checkout: str = Field(alias = "checkOut")


class BookingModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    firstname: str = Field(alias = "firstName")
    lastname: str = Field(alias = "lastName")
    totalprice: int = Field(alias = "totalPrice")
    depositpaid: bool = Field(alias = "depositPaid")
    bookingdates: BookingDatesModel = Field(alias = "bookingDates")
    additionalneeds: str = Field(alias = "additionalNeeds", default=None)

class BookingIdModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    bookingid: int = Field(alias = "bookingId")

class CreateBookingResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    bookingid: int = Field(alias = "bookingId")
    booking: BookingModel = Field(alias = "booking")