"""Database connection manager for the booking domain.

This module provides functionality for creating and managing
SQLAlchemy sessions connected to the booking SQLite database.
"""

import sqlite3
from sqlite3 import Connection

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.common.common_paths import CommonPaths
from src.db.booking.db_models.booking_db_model import Base


class BookingDB:
    """Factory class responsible for creating booking database sessions."""

    def connect_sql_alchemy(self) -> Session:
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

    def connect_cursor(self) -> Connection:
        """Create and return a SQLite database connection.

        This method establishes a connection to the booking test database
        located in the project's test resources directory.

        Returns:
            Connection: Active SQLite database connection object.
        """
        return sqlite3.connect(f'{CommonPaths.project_root().joinpath("tests").joinpath("resources")}/booking.db')
