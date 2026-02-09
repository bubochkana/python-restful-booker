from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
class Base(DeclarativeBase):
    pass

class BookingDB(Base):
    __tablename__ = "booking"
    bookingid: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(256))
    lastname: Mapped[str] = mapped_column(String(256))
    totalprice: Mapped[int]
    depositpaid: Mapped[bool]
    checkin: Mapped[str] = mapped_column(String(20))
    checkout: Mapped[str] = mapped_column(String(20))
    additionalneeds:Mapped[Optional[str]] = mapped_column(String(256))

    def __repr__(self) -> str:
        return (f"Booking("
                f"bookingid={self.bookingid!r}, "
                f"firstname={self.firstname!r}, "
                f"lastname={self.lastname!r}, "
                f"totalprice={self.totalprice!r}), "
                f"depositpaid={self.depositpaid!r}), "
                f"checkin={self.checkin!r}), "
                f"checkout={self.checkout!r}), "
                f"addiitonalneeds={self.addiitonalneeds!r}), "
                )
