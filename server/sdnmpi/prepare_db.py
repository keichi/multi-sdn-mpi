from .models import db, Job, Process


MODELS = [
    Job,
    Process
]


if __name__ == "__main__":
    with db:
        db.create_tables(MODELS)
