CXX = g++
PROTOC = protoc
CPPFLAGS += `pkg-config --cflags protobuf grpc`
CXXFLAGS += -std=c++11
LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++`

PROTOS_PATH = "../protos"

all: sdnmpi.so client_test

%.o: %.cc
	$(CXX) -o $@ -c $(CPPFLAGS) $(CXXFLAGS) $^

%.grpc.pb.cc: %.proto
	$(PROTOC) -I $(PROTOS_PATH) --grpc_out=. --plugin=protoc-gen-grpc=$(GRPC_CPP_PLUGIN_PATH) $<

%.pb.cc: %.proto
	$(PROTOC) -I $(PROTOS_PATH) --cpp_out=. $<

sdnmpi.so: src/sdnmpi.o sdnmpi.pb.o sdnmpi.grpc.pb.o
	$(CXX) -o $@ -shared -fPIC $(LDFLAGS) $^

client_test: src/client_test.o sdnmpi.pb.o sdnmpi.grpc.pb.o
	$(CXX) -o $@ $(LDFLAGS) $^
