from typing import List

from pydantic import BaseModel, ConfigDict


class BaseCategory(BaseModel):
    title: str


class CategoryIn(BaseCategory):
    ...


class CategoryOut(BaseCategory):
    id: int

    class ConfigDict:
        from_attributes = True


class BaseShoes(BaseModel):
    title: str
    quantity: int
    price: int
    category_id: int


class ShoesIn(BaseShoes):
    ...


class ShoesOut(BaseShoes):
    id: int

    class ConfigDict:
        from_attributes = True


class SettingForCustomSort(BaseModel):
    category_id: int
    price_range: List[int]
    quantity: int
