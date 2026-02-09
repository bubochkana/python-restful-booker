from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

from src.models.bookings.sql_alchemy_booking_model import Base, BookingDB


class SqlAlchemyManager:
    def __init__(self):
        self.engine = create_engine("sqlite://", echo=True)
        Base.metadata.create_all(self.engine)

        with Session(self.engine) as self.session:
            booking = BookingDB(
                bookingid=1,
                firstname="Gabriella",
                lastname="Soliz",
                totalprice=300,
                depositpaid=True,
                checkin="2024-11-25",
                checkout="2024-12-07",
                additionalneeds="A bed for a child"
            )
            self.session.add_all([booking])
            self.session.commit()

    def select_booking(self, booking_id) -> BookingDB:
        return self.session.scalar(select(BookingDB).where(BookingDB.bookingid == booking_id))