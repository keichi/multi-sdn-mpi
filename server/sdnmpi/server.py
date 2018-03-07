from concurrent.futures import ThreadPoolExecutor
import logging
import time

import colorlog
import grpc

from .sdnmpi_pb2_grpc import add_SDNMPIServicer_to_server
from .servicer import SDNMPIServicer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


logger = logging.getLogger(__name__)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_SDNMPIServicer_to_server(SDNMPIServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


def setup_logging():
    handler = colorlog.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s[%(levelname)s]%(reset)s [%(name)s]: %(message)s"
    )
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


if __name__ == "__main__":
    setup_logging()
    serve()
