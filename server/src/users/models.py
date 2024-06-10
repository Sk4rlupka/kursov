from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    discount_id = Column(Integer, ForeignKey("discount.id"))
    discount = relationship("Discount", uselist=False)
    parking_info = relationship("ParkingInfo", uselist=False)
