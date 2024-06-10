from pydantic import BaseModel


class TariffPriceCreate(BaseModel):
    name: str
    description: str
    price_per_hour: float


class TariffPriceUpdate(TariffPriceCreate):
    id: int

