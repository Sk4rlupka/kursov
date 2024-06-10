from fastapi import APIRouter, Depends

from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from users.models import User
from users.schemas import UserCreate, UserUpdate

from parking_info.models import ParkingInfo

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
async def get_users(
        session: AsyncSession = Depends(get_async_session),
):
    query = (
        select(User)
        .options(
            selectinload(User.parking_info)
            .options(joinedload(ParkingInfo.tariff_price))
        )
        .options(joinedload(User.discount))
    )

    return (await session.execute(query)).scalars().all()


@router.post("/")
async def add_users(
        user: UserCreate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(User).values(**user.model_dump())

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.put("/")
async def update_users(
        user: UserUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = update(User).values(**user.model_dump()).filter_by(id=user.id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/")
async def delete_users(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = delete(User).filter_by(id=user_id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}
