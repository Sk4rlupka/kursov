from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base

from datetime import datetime


class ParkingInfo(Base):
    __tablename__ = "parking_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kind_of_car = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", uselist=False, viewonly=True)
    date_of_entry = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    date_of_departure = Column(TIMESTAMP(timezone=True))
    date_paid_for = Column(TIMESTAMP(timezone=True))
    tariff_price_id = Column(Integer, ForeignKey("tariff_price.id"))
    tariff_price = relationship("TariffPrice", uselist=False)
