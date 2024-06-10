from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base

from datetime import datetime


class Discount(Base):
    __tablename__ = "discount"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    percentage = Column(Float)
