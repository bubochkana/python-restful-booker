"""SQLAlchemy ORM models for booking persistence.

This module defines the declarative base and ORM mappings used to persist
booking-related data in the database. The models are designed to align with
the booking API domain and support CRUD operations via SQLAlchemy sessions.
"""

from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Declarative base class for SQLAlchemy ORM models.

    All database models in the application should inherit from this base
    to ensure consistent metadata handling and ORM configuration.
    """

    pass


class BookingDBModel(Base):
    """SQLAlchemy ORM model representing a booking record.

    This model maps to the ``booking`` database table and stores all
    booking-related fields such as customer name, pricing information,
    booking dates, and optional additional needs.
    """

    __tablename__ = 'booking'
    bookingid: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(256))
    lastname: Mapped[str] = mapped_column(String(256))
    totalprice: Mapped[int]
    depositpaid: Mapped[bool]
    checkin: Mapped[str] = mapped_column(String(20))
    checkout: Mapped[str] = mapped_column(String(20))
    additionalneeds: Mapped[Optional[str]] = mapped_column(String(256))

    def __repr__(self) -> str:
        """Return a string representation of the booking record.

        This representation is intended for debugging and logging purposes
        and includes key identifying and descriptive fields of the booking.

        Returns:
            str: String representation of the booking entity.
        """
        return (
            f'Booking('
            f'bookingid={self.bookingid!r}, '
            f'firstname={self.firstname!r}, '
            f'lastname={self.lastname!r}, '
            f'totalprice={self.totalprice!r}), '
            f'depositpaid={self.depositpaid!r}), '
            f'checkin={self.checkin!r}), '
            f'checkout={self.checkout!r}), '
            f'addiitonalneeds={self.addiitonalneeds!r}), '
        )
