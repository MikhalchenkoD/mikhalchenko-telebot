import pytest
from httpx import AsyncClient

from api_for_telebot.main import schemas
from api_for_telebot.main.app import app


async def test_create_category():
    category_data = {"title": "Туфли"}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/category/", json=category_data)

    category_out = schemas.CategoryOut(**response.json())
    assert isinstance(category_out, schemas.CategoryOut)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_shoes():
    shoes_data = {
        "title": "Супер туфли",
        "quantity": 2,
        "price": 10000,
        "category_id": 1,
    }

    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/shoes/", json=shoes_data)

    shoes_out = schemas.ShoesOut(**response.json())
    assert isinstance(shoes_out, schemas.ShoesOut)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_shoes():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/shoes")

    assert len(response.json()) > 0
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_category():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/category")

    assert len(response.json()) > 0
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_cheap_shoes():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/shoes/cheap/1")

    assert response.json()[0]["price"] <= response.json()[-1]["price"]
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_expensive_shoes():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/shoes/expensive/1")

    assert response.json()[0]["price"] >= response.json()[-1]["price"]
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_custom_shoes():
    setting_data = {"category_id": 1, "price_range": [5000, 50000], "quantity": 3}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/shoes/custom", json=setting_data)

    assert response.json()[0]["price"] >= response.json()[-1]["price"]
    assert response.json()[0]["price"] >= setting_data["price_range"][0]
    assert response.json()[-1]["price"] <= setting_data["price_range"][1]
    assert len(response.json()) <= setting_data["quantity"]
    assert response.status_code == 200
