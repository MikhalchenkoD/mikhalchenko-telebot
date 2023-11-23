from datetime import datetime
from database.models.history import History
from loader import database
import pickle


def set_history(user_id, request_info: str, response_info: list) -> None:
    response = pickle.dumps(response_info)
    History.get_or_create(user_id=user_id, date_time=datetime.now(), request_info=request_info,
                          response_info=response)


def get_all_history(user_id: int) -> list:
    query = History.select().where(History.user_id == user_id).order_by(History.date_time).dicts().execute()
    return list(query)


if database.table_exists(History) is False:
    database.create_tables([History])
