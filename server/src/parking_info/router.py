from fastapi import APIRouter, Depends

from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from parking_info.models import ParkingInfo
from parking_info.schemas import ParkingInfoCreate, ParkingInfoUpdate

from users.models import User

from datetime import datetime

router = APIRouter(
    prefix="/parking_info",
    tags=["Parking Info"]
)


@router.get("/")
async def get_parking_info(
        session: AsyncSession = Depends(get_async_session),
):
    query = select(ParkingInfo)

    return (await session.execute(query)).scalars().all()


@router.get("/arrears/{parking_info_id}")
async def get_users_arrears(parking_info_id: int, session: AsyncSession = Depends(get_async_session)):
    parking_info_query = (
        select(ParkingInfo)
        .options(
            joinedload(ParkingInfo.tariff_price),
            joinedload(ParkingInfo.owner).options(joinedload(User.discount))
        )
        .filter_by(id=parking_info_id)
    )
    parking_info = (await session.execute(parking_info_query)).scalar()

    date_start = parking_info.date_paid_for.replace(tzinfo=None) if parking_info.date_paid_for else parking_info.date_of_entry.replace(tzinfo=None)
    date_end = datetime.utcnow() if not parking_info.date_of_departure else parking_info.date_of_departure.replace(tzinfo=None)

    hours = abs(date_start - date_end).total_seconds() / 3600.0
    price = hours * parking_info.tariff_price.price_per_hour

    if parking_info.owner.discount:
        price -= price * parking_info.owner.discount.percentage

    if date_end > date_start:
        return f"Задолженность в {round(price, 2)} руб."
    elif date_end < date_start:
        return f"Предоплата/cдача на {round(price, 2)}"
    else:
        return "Задолженности нет"

@router.post("/")
async def add_parking_info(
        parking_info: ParkingInfoCreate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(ParkingInfo).values(**parking_info.model_dump())

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.put("/")
async def update_parking_info(
        parking_info: ParkingInfoUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = update(ParkingInfo).values(**parking_info.model_dump()).filter_by(id=parking_info.id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/")
async def delete_parking_info(
        parking_info_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = delete(ParkingInfo).filter_by(id=parking_info_id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}
