"""Query manager for booking-related database operations.

This module provides a small abstraction layer over SQLAlchemy ORM queries
used to retrieve booking records from the database. It is designed to work
with externally managed SQLAlchemy sessions, such as those provided by
pytest fixtures or application-level session factories.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.bookings.sql_alchemy_booking_model import BookingDBModel


class SqlAlchemyQueryManager:
    """Query manager for booking-related database operations using SQLAlchemy.

    This class provides a thin abstraction layer over SQLAlchemy ORM queries
    related to the ``BookingDB`` model. It operates on a SQLAlchemy
    ``Session`` instance that must be provided externally, allowing the
    session lifecycle to be controlled by the caller (for example, via
    pytest fixtures or application-level session management).
    """

    def __init__(self, session: Session):
        """Initialize the query manager with an active SQLAlchemy session.

        Args:
            session: An active SQLAlchemy ``Session`` bound to the target
                database engine.
        """
        self.session = session

    def select_booking(self, booking_id) -> BookingDBModel:
        """Retrieve a booking record by its unique identifier.

        Executes a SELECT query against the ``BookingDB`` table and returns
        the matching booking entity if found.

        Args:
            booking_id: Unique identifier of the booking to retrieve.

        Returns:
            BookingDBModel | None: The matching booking record if it exists,
            otherwise ``None``.
        """
        return self.session.scalar(select(BookingDBModel).where(BookingDBModel.bookingid == booking_id))
