from fastapi import APIRouter, Depends

from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from discounts.models import Discount
from discounts.schemas import DiscountCreate, DiscountUpdate

router = APIRouter(
    prefix="/discount",
    tags=["Discount"]
)


@router.get("/")
async def get_discounts(
        session: AsyncSession = Depends(get_async_session),
):
    query = select(Discount)

    return (await session.execute(query)).scalars().all()


@router.post("/")
async def add_discount(
        discount: DiscountCreate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(Discount).values(**discount.model_dump())

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.put("/")
async def update_discount(
        discount: DiscountUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = update(Discount).values(**discount.model_dump()).filter_by(id=discount.id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/")
async def delete_discount(
        discount_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = delete(Discount).filter_by(id=discount_id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}
