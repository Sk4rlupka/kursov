from fastapi import FastAPI, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from users.router import router as users_router
from parking_info.router import router as parking_info_router
from tariff_prices.router import router as tariff_prices_router
from discounts.router import router as discounts_router

from pages.router import router as pages_router

app = FastAPI(
    title="Система автостоянка"
)

# Серверные роутеры
app.include_router(users_router)
app.include_router(parking_info_router)
app.include_router(tariff_prices_router)
app.include_router(discounts_router)


# Клиентские роутеры
app.include_router(pages_router)
