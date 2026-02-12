from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.common.common_paths import CommonPaths
from src.db.booking.db_models.booking_db_model import Base


class BookingDB:
    def connect(self) -> Session:
        engine = create_engine(
            f'sqlite:////{CommonPaths.project_root().joinpath("tests").joinpath("resources")}/booking.db', echo=True
        )
        Base.metadata.create_all(engine)

        with Session(engine) as session:
            return session
