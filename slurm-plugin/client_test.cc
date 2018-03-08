#include <grpc++/grpc++.h>

#include  "sdnmpi.grpc.pb.h"

int main(int argc, char **argv)
{
    const auto cred = grpc::InsecureChannelCredentials();
    const auto chan = grpc::CreateChannel("localhost:50051", cred);
    const auto stub = SDNMPI::NewStub(chan);

    Empty request;
    ListJobResponse response;
    grpc::ClientContext context;

    auto status = stub->ListJob(&context, request, &response);

    if (status.ok()) {
        std::cout << "ok!" << std::endl;

        for (const auto& job : response.jobs()) {
            std::cout << job.id() << std::endl;
        }
    } else {
        std::cout << "ng!" << std::endl;
    }

    return 0;
}
