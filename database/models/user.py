from peewee import CharField, Model, DateTimeField
from datetime import datetime
from database.database import db


class User(Model):
    name = CharField()
    email = CharField()
    password = CharField()
    date = DateTimeField(default=datetime.now())

    class Meta:
        database = db 