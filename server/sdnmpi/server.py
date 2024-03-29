import logging
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import colorlog

import grpc

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .sdnmpi_pb2_grpc import add_SDNMPIServicer_to_server
from .servicer import SDNMPIServicer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
GRPC_SERVER_ADDRESS = "0.0.0.0:50051"


logger = logging.getLogger(__name__)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=1))
    servicer = SDNMPIServicer()
    add_SDNMPIServicer_to_server(servicer, server)
    server.add_insecure_port(GRPC_SERVER_ADDRESS)
    server.start()

    logger.info("gRPC server started on %s", GRPC_SERVER_ADDRESS)

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
