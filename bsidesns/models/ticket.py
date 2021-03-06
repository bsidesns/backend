import datetime

from freenit.db import db
from peewee import BooleanField, DateTimeField, ForeignKeyField, TextField

from ..date import datetime_format
from .event import Event
from .user import User

Model = db.Model


class Ticket(Model):
    canceled = BooleanField(default=False)
    identifier = TextField()
    date = DateTimeField(
        formats=[datetime_format],
        default=datetime.datetime.utcnow
    )
    event = ForeignKeyField(Event, backref='tickets')
    visitor = ForeignKeyField(User, backref='tickets')
