HOST_SYSTEM = $(shell uname | cut -f 1 -d_)
SYSTEM ?= $(HOST_SYSTEM)
CXX = g++
PROTOC = protoc
CPPFLAGS += `pkg-config --cflags protobuf grpc++`
CXXFLAGS += -std=c++11
LDFLAGS += `pkg-config --libs protobuf grpc++`

ifeq ($(SYSTEM),Darwin)
	LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc`\
				-lgrpc++_reflection\
				-ldl
else
	LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++ grpc`\
				-Wl,--no-as-needed -lgrpc++_reflection -Wl,--as-needed\
				-ldl
endif

PROTOS_PATH = ../protos
GRPC_CPP_PLUGIN = grpc_cpp_plugin
GRPC_CPP_PLUGIN_PATH = `which $(GRPC_CPP_PLUGIN)`

# .SUFFIXES: .proto .grpc.pb.cc .pb.cc

vpath %.proto $(PROTOS_PATH)

all: sdnmpi.so client_test

%.o: %.cc
	$(CXX) -o $@ -c -fPIC $(CPPFLAGS) $(CXXFLAGS) $^

.PRECIOUS: %.grpc.pb.cc
%.grpc.pb.cc: %.proto
	$(PROTOC) -I $(PROTOS_PATH) --grpc_out=. --plugin=protoc-gen-grpc=$(GRPC_CPP_PLUGIN_PATH) $<

.PRECIOUS: %.pb.cc
%.pb.cc: %.proto
	$(PROTOC) -I $(PROTOS_PATH) --cpp_out=. $<

sdnmpi.so: sdnmpi.o  sdnmpi.pb.o sdnmpi.grpc.pb.o
	$(CXX) -o $@ -shared -fPIC $(LDFLAGS) $^

client_test: client_test.o sdnmpi.pb.o sdnmpi.grpc.pb.o
	$(CXX) -o $@ $(LDFLAGS) $^

clean:
	rm -f *.o *.so
