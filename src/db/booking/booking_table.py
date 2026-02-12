import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.booking.db_models.booking_db_model import BookingDBModel


class BookingTable:
    def __init__(self, session: Session):
        self.session = session

    def booking_table(self):
        return self

    def get_by_id(self, booking_id):
        stmt = select(BookingDBModel).where(BookingDBModel.bookingid == booking_id)
        return self.session.scalar(stmt)

    def get_all(self):
        stmt = select(BookingDBModel)
        return self.session.scalars(stmt).all()

    def as_data_frame(self):
        stmt = select(BookingDBModel)
        result = self.session.execute(stmt).mappings().all()
        return pd.DataFrame(result)
