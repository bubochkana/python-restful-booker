"""Database connection manager for the booking domain.

This module provides functionality for creating and managing
SQLAlchemy sessions connected to the booking SQLite database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.common.common_paths import CommonPaths
from src.db.booking.db_models.booking_db_model import Base


class BookingDB:
    """Factory class responsible for creating booking database sessions."""

    def connect(self) -> Session:
        """Create and return a SQLAlchemy session connected to the booking database.

        The database engine is initialized using a SQLite file located in the
        test resources directory. The database schema is created if it does
        not already exist.

        Returns:
            Session: Active SQLAlchemy session bound to the booking database.
        """
        engine = create_engine(
            f'sqlite:////{CommonPaths.project_root().joinpath("tests").joinpath("resources")}/booking.db', echo=True
        )
        Base.metadata.create_all(engine)

        with Session(engine) as session:
            return session
