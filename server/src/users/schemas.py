from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str | None
    surname: str | None
    name: str | None
    patronymic: str | None
    discount_id: int | None


class UserUpdate(UserCreate):
    id: int
