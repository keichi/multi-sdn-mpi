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
    "stencil2d-32",
    "stencil2d-64",
    "stencil2d-128",
    "stencil2d-160",
    "stencil3d-32",
    "stencil3d-64",
    "stencil3d-100",
    "stencil3d-120",
    "stencil3d-128",
    "stencil3d-150",
    "stencil3d-160",
    "spmv-32",
    "spmv-64",
    "spmv-128",
    "butterfly-32",
    "butterfly-64",
    "butterfly-128"
]


def _load_json(f, pattern):
    trace = json.loads(f.read().decode("utf-8"))

    n_procs = trace["n_procs"]
    src = trace["rank"]

    pattern.duration = max(pattern.duration, trace["duration"])

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

    pattern.save()


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

        pattern = CommPattern.create(name=name, duration=0.0)

        with open("fixtures/" + name + ".tar.gz", "rb") as f:
            _load_tarball(f, pattern)


def main():
    with db:
        db.create_tables(MODELS)
        _load_fixtures()


if __name__ == "__main__":
    main()
