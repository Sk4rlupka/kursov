from pydantic import BaseModel


class DiscountCreate(BaseModel):
    name: str
    description: str
    percentage: float


class DiscountUpdate(DiscountCreate):
    id: int
