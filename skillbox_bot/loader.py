from peewee import SqliteDatabase
from telebot import asyncio_filters
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
bot = AsyncTeleBot(config.BOT_TOKEN, state_storage=storage)
database = SqliteDatabase(config.DATABASE)
