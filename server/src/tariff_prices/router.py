from fastapi import APIRouter, Depends

from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from tariff_prices.models import TariffPrice
from tariff_prices.schemas import TariffPriceCreate, TariffPriceUpdate

router = APIRouter(
    prefix="/tariff_prices",
    tags=["Tariff Prices"]
)


@router.get("/")
async def get_tariff_prices(
        session: AsyncSession = Depends(get_async_session),
):
    query = select(TariffPrice)

    return (await session.execute(query)).scalars().all()


@router.post("/")
async def add_tariff_prices(
        tariff_prices: TariffPriceCreate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(TariffPrice).values(**tariff_prices.model_dump())

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.put("/")
async def update_tariff_prices(
        tariff_prices: TariffPriceUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = update(TariffPrice).values(**tariff_prices.model_dump()).filter_by(id=tariff_prices.id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/")
async def delete_tariff_prices(
        tariff_prices_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = delete(TariffPrice).filter_by(id=tariff_prices_id)

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}
