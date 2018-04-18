from enum import Enum

from peewee import CharField, ForeignKeyField, IntegerField
from peewee import Model, SqliteDatabase

db = SqliteDatabase("sdnmpi.db")


class BaseModel(Model):
    class Meta:
        database = db


class JobState(Enum):
    PENDING = 0
    RUNNING = 1
    COMPLETE = 2


class Job(BaseModel):
    uid = IntegerField()
    gid = IntegerField()
    comm_pattern = CharField()
    name = CharField()
    n_tasks = IntegerField()
    n_started = IntegerField(default=0)
    n_exited = IntegerField(default=0)
    state = IntegerField(default=JobState.PENDING.value)

    class Meta:
        table_name = "job"


class ProcessState(Enum):
    PENDING = 0
    RUNNING = 1
    COMPLETE = 2


class Process(BaseModel):
    job = ForeignKeyField(Job, backref="processes")
    rank = IntegerField()
    node_id = IntegerField()
    node_name = CharField()
    state = IntegerField(default=ProcessState.PENDING.value)

    class Meta:
        table_name = "process"
        indexes = (
            (("job", "rank"), True),
        )


class CommPattern(BaseModel):
    name = CharField(index=True)

    class Meta:
        table_name = "comm_pattern"


class CommPair(BaseModel):
    pattern = ForeignKeyField(CommPattern, backref="pairs")
    src = IntegerField()
    dst = IntegerField()
    tx_bytes = IntegerField()
    rx_bytes = IntegerField()
    tx_messages = IntegerField()
    rx_messages = IntegerField()

    class Meta:
        table_name = "comm_pair"

        indexes = (
            (("pattern", "src", "dst"), True),
        )
