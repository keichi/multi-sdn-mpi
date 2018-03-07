from enum import Enum

from peewee import Model, SqliteDatabase
from peewee import CharField, IntegerField, ForeignKeyField

db = SqliteDatabase("sdnmpi.db")


class BaseModel(Model):
    class Meta:
        database = db


class JobState(Enum):
    PENDING = 0
    RUNNING = 1
    COMPLETE = 2


class Job(BaseModel):
    id = IntegerField(primary_key=True)
    uid = IntegerField()
    gid = IntegerField()
    comm_pattern = CharField()
    name = CharField()
    n_tasks = IntegerField()
    state = IntegerField()


class ProcessState(Enum):
    PENDING = 0
    RUNNING = 1
    COMPLETE = 2


class Process(BaseModel):
    id = IntegerField(primary_key=True)
    job = ForeignKeyField(Job, backref="processes")
    rank = IntegerField()
    node_id = IntegerField()
    node_name = CharField()
    state = IntegerField()

    class Meta:
        indexes = (
            (("job", "rank"), True),
        )
