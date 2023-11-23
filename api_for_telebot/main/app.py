from contextlib import asynccontextmanager
from typing import List, Sequence

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import api_for_telebot.main.models as models
from api_for_telebot.main.database import engine, get_async_session
import api_for_telebot.main.schemas as schemas
import uvicorn

from api_for_telebot.main.models import Shoes


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/category/", response_model=schemas.CategoryOut)
async def add_new_category_in_db(
    category: schemas.CategoryIn, session: AsyncSession = Depends(get_async_session)
) -> models.Category:
    new_category = models.Category(**category.model_dump())
    async with session.begin():
        session.add(new_category)
    return new_category


@app.get("/category", response_model=List[schemas.CategoryOut])
async def get_all_category_from_db(
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[models.Category]:
    res = await session.execute(select(models.Category))
    return res.scalars().all()


@app.post("/shoes/", response_model=schemas.ShoesOut)
async def add_new_shoes_in_db(
    shoes: schemas.ShoesIn, session: AsyncSession = Depends(get_async_session)
) -> models.Shoes:
    new_shoes = models.Shoes(**shoes.model_dump())
    async with session.begin():
        session.add(new_shoes)
    return new_shoes


@app.get("/shoes", response_model=List[schemas.ShoesOut])
async def get_all_shoes_from_db(
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Shoes]:
    res = await session.execute(select(models.Shoes))
    return res.scalars().all()


@app.get("/shoes/cheap/{category_id}", response_model=List[schemas.ShoesOut])
async def get_cheap_products(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> List[models.Shoes]:
    res = await session.execute(
        select(models.Shoes)
        .order_by(models.Shoes.price.asc())
        .where(models.Shoes.category_id == category_id)
    )
    return res.scalars().all()


@app.get("/shoes/expensive/{category_id}", response_model=List[schemas.ShoesOut])
async def get_expensive_products(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> List[models.Shoes]:
    res = await session.execute(
        select(models.Shoes)
        .order_by(models.Shoes.price.desc())
        .where(models.Shoes.category_id == category_id)
    )

    return res.scalars().all()


@app.post("/shoes/custom", response_model=List[schemas.ShoesOut])
async def get_custom_products(
    custom_settings: schemas.SettingForCustomSort,
    session: AsyncSession = Depends(get_async_session),
) -> List[models.Shoes]:
    res = await session.execute(
        select(models.Shoes)
        .order_by(models.Shoes.price)
        .where(
            models.Shoes.category_id == custom_settings.category_id,
            models.Shoes.price >= custom_settings.price_range[0],
            models.Shoes.price <= custom_settings.price_range[1],
        )
        .limit(custom_settings.quantity)
    )

    return res.scalars().all()


if __name__ == "__main__":
    uvicorn.run(app)
