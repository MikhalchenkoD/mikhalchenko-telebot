from database.models import User
from telebot.types import Message
from datetime import datetime
from loader import database


def get_or_create_user(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        user = User.get_or_create(first_name=message.from_user.first_name, last_name=message.from_user.last_name,
                                  user_id=message.from_user.id, username=message.from_user.username,
                                  create_date=datetime.now())

    return user


def get_user(user_id: int) -> User:
    return User.get_or_none(User.user_id == user_id)


def get_users() -> list[User]:
    query = User.select().dicts().execute()
    return query


if database.table_exists(User) is False:
    database.create_tables([User])
