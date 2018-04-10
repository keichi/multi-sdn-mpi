import json
import tarfile

from .models import CommPair, CommPattern, Job, Process, db


MODELS = [
    Job,
    Process,
    CommPattern,
    CommPair
]

PATTERN_NAMES = [
    "cg-c-8",
    "cg-c-16",
    "cg-c-32",
    "cg-c-64",
    "cg-c-128",
    "ft-d-8",
    "ft-d-16",
    "ft-d-32",
    "ft-c-128",
    "minife-small-128",
    "minife-small-160",
    "minife-tiny-16",
    "minife-tiny-32",
    "minife-tiny-64",
    "minife-tiny-128",
    "minife-tiny-160",
    "minighost-small-128",
    "minighost-small-160",
    "minighost-tiny-16",
    "minighost-tiny-32",
    "minighost-tiny-64",
    "minighost-tiny-128",
    "minighost-tiny-160",
]


def _load_json(f, pattern):
    trace = json.loads(f.read().decode("utf-8"))

    n_procs = trace["n_procs"]
    src = trace["rank"]

    for dst in range(n_procs):
        tx_messages = trace["tx_messages"][dst]
        rx_messages = trace["rx_messages"][dst]
        tx_bytes = trace["tx_bytes"][dst]
        rx_bytes = trace["rx_bytes"][dst]

        if tx_messages == 0 and rx_messages == 0:
            continue

        CommPair.create(
            pattern=pattern,
            src=src,
            dst=dst,
            tx_bytes=tx_bytes,
            rx_bytes=rx_bytes,
            tx_messages=tx_messages,
            rx_messages=rx_messages
        )


def _load_tarball(f, pattern):
    with tarfile.open(fileobj=f, mode="r:*") as tar:
        for member in tar.getmembers():
            if not member.isfile() or not member.name.endswith(".json"):
                continue

            with tar.extractfile(member) as f:
                _load_json(f, pattern)


def _load_fixtures():
    for name in PATTERN_NAMES:
        print("Loading", name)

        pattern = CommPattern.create(name=name)

        with open("fixtures/" + name + ".tar.gz", "rb") as f:
            _load_tarball(f, pattern)


def main():
    with db:
        db.create_tables(MODELS)
        _load_fixtures()


if __name__ == "__main__":
    main()
