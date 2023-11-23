import asyncio
from typing import Generator, Iterator, AsyncGenerator

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from api_for_telebot.main.models import Base, Shoes, Category
from api_for_telebot.main.database import get_async_session

from api_for_telebot.main.app import app

DATABASE_URL_TEST = "postgresql+asyncpg://postgres:1234@localhost/test_telebot"
engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
TestingSessionLocal = sessionmaker(
    engine_test, class_=AsyncSession, expire_on_commit=False
)


async def override_get_async_session():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        await db.close()


app.dependency_overrides[get_async_session] = override_get_async_session


# @pytest.fixture(scope='session')
# def event_loop(request):
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture(scope="session")
async def prepare_database(request):
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
