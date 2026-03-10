"""Booking table query layer.

This module provides a database query interface for interacting with
the booking table using SQLAlchemy ORM and optional pandas integration.
"""

from typing import Optional

from sqlalchemy.orm import Session

from src.db.abstract_table import AbstractTable
from src.db.booking.db_models.booking_db_model import BookingDBModel


class BookingTable(AbstractTable[BookingDBModel]):
    """Query interface for booking-related database operations.

    Extends:
        AbstractTable: Provides generic CRUD-style query helpers.

    Args:
        session (Session): Active SQLAlchemy session.
    """

    def __init__(self, session: Session):
        """Initialize the booking table query interface.

        Args:
            session (Session): Active SQLAlchemy session used to execute queries.
        """
        super().__init__(BookingDBModel, session)

    def booking_table(self) -> 'BookingTable':
        """Return the current BookingTable instance.

        This method acts as a convenience accessor and returns
        the current object instance.

        Returns:
            BookingTable: The current instance.
        """
        return self

    def get_by_id(self, booking_id: int) -> Optional[BookingDBModel]:
        """Retrieve a booking record by its unique identifier.

        Args:
            booking_id (int): Identifier of the booking to retrieve.

        Returns:
            Optional[BookingDBModel]: Matching booking ORM object if found,
            otherwise ``None``.
        """
        return super().get_by(BookingDBModel.bookingid == booking_id)
