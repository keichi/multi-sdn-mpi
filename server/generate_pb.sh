#!/bin/bash

 python -m grpc.tools.protoc -I ../protos --python_out=. --grpc_python_out=. sdnmpi/sdnmpi.proto
