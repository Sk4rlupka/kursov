from pydantic import BaseModel

from datetime import datetime


class ParkingInfoCreate(BaseModel):
    kind_of_car: str | None
    owner_id: int | None
    date_of_entry: datetime | None
    date_of_departure: datetime | None
    date_paid_for: datetime | None
    tariff_price_id: int | None


class ParkingInfoUpdate(ParkingInfoCreate):
    id: int
