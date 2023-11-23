from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, BlobField
from .base import BaseModel
from .user import User


class History(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(User, 'user_id')
    date_time = DateTimeField()
    request_info = CharField()
    response_info = BlobField()

    class Meta:
        table_name = 'history'
