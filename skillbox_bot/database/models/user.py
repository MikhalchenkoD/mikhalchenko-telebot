from peewee import IntegerField, CharField, DateTimeField
from .base import BaseModel


class User(BaseModel):
    id = IntegerField(primary_key=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    user_id = IntegerField()
    username = CharField(null=True)
    create_date = DateTimeField()

    class Meta:
        table_name = 'users'
