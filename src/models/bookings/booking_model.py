"""Pydantic models for booking API data.

This module defines Pydantic models representing booking-related
request and response payloads, including booking details, booking
dates, and booking identifiers.
"""

from pydantic import BaseModel, ConfigDict, Field


class BookingDatesModel(BaseModel):
    """Model representing booking dates information.

    This model maps check in and check out dates between Python field
    names and API field aliases.
    """

    model_config = ConfigDict(populate_by_name=True)

    checkin: str = Field(alias="checkIn")
    checkout: str = Field(alias="checkOut")


class BookingModel(BaseModel):
    """Model representing a booking request (create, update or patch) or response (update and patch).

    This model contains all booking-related details.
    """

    model_config = ConfigDict(populate_by_name=True)

    firstname: str = Field(alias="firstName")
    lastname: str = Field(alias="lastName")
    totalprice: int = Field(alias="totalPrice")
    depositpaid: bool = Field(alias="depositPaid")
    bookingdates: BookingDatesModel = Field(alias="bookingDates")
    additionalneeds: str = Field(alias="additionalNeeds", default=None)


class BookingIdModel(BaseModel):
    """Model representing a booking identifier.

    This model is used for listing of bookings when only the booking identifier is returned
    by the API.
    """

    model_config = ConfigDict(populate_by_name=True)

    bookingid: int = Field(alias="bookingId")


class CreateBookingResponse(BaseModel):
    """Model representing the response from a booking creation request.

    This model includes the newly created booking identifier and the
    full booking details returned by the API.
    """

    model_config = ConfigDict(populate_by_name=True)

    bookingid: int = Field(alias="bookingId")
    booking: BookingModel = Field(alias="booking")
