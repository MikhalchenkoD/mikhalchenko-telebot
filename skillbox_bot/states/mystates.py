from telebot.asyncio_handler_backends import StatesGroup, State


class CustomSearch(StatesGroup):
    price_range = State()
    quantity = State()
