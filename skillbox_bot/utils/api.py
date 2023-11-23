import aiohttp
from typing import List

BASE_URL = 'http://127.0.0.1:8000'


async def get_low_product(category_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}/shoes/cheap/{category_id}') as response:
            return await response.json()


async def get_high_product(category_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}/shoes/expensive/{category_id}') as response:
            return await response.json()


async def get_custom_product(category_id: int, price_range: List[int], quantity: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{BASE_URL}/shoes/custom', json={
            "category_id": category_id,
            "price_range": price_range,
            "quantity": quantity
        }) as response:
            return await response.json()


async def get_all_products():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}/shoes') as response:
            return await response.json()


async def get_all_category():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}/category') as response:
            return await response.json()



