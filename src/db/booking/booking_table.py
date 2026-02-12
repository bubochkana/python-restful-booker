"""Booking table query layer.

This module provides a database query interface for interacting with
the booking table using SQLAlchemy ORM and optional pandas integration.
"""

import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.booking.db_models.booking_db_model import BookingDBModel


class BookingTable:
    """Query interface for booking-related database operations."""

    def __init__(self, session: Session):
        """Initialize the booking table query interface.

        Args:
            session: Active SQLAlchemy session used to execute queries.
        """
        self.session = session

    def booking_table(self) -> 'BookingTable':
        """Return the current BookingTable instance.

        This method acts as a convenience accessor and returns
        the current object instance.

        Returns:
            BookingTable: The current instance.
        """
        return self

    def get_by_id(self, booking_id):
        """Retrieve a booking record by its unique identifier.

        Args:
            booking_id: Identifier of the booking to retrieve.

        Returns:
            BookingDBModel | None: The matching booking entity if found,
            otherwise ``None``.
        """
        stmt = select(BookingDBModel).where(BookingDBModel.bookingid == booking_id)
        return self.session.scalar(stmt)

    def get_all(self):
        """Retrieve all booking records from the database.

        Returns:
            list[BookingDBModel]: List of all booking ORM entities.
        """
        stmt = select(BookingDBModel)
        return self.session.scalars(stmt).all()

    def as_data_frame(self):
        """Retrieve all booking records as a pandas DataFrame.

        Executes a SELECT statement and converts the result
        mappings into a pandas DataFrame.

        Returns:
            pandas.DataFrame: DataFrame containing booking records.
        """
        stmt = select(BookingDBModel)
        result = self.session.execute(stmt).mappings().all()
        return pd.DataFrame(result)
