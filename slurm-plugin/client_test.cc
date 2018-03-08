#include <grpc++/grpc++.h>

#include  "sdnmpi.grpc.pb.h"

int main(int argc, char **argv)
{
    const auto cred = grpc::InsecureChannelCredentials();
    const auto chan = grpc::CreateChannel("localhost:50051", cred);
    const auto stub = SDNMPI::NewStub(chan);

    // Empty request;
    // ListJobResponse response;
    // grpc::ClientContext context;

    // auto status = stub->ListJob(&context, request, &response);

    // if (status.ok()) {
    //     std::cout << "ok!" << std::endl;

    //     for (const auto& job : response.jobs()) {
    //         std::cout << job.id() << std::endl;
    //     }
    // } else {
    //     std::cout << "ng!" << std::endl;
    // }

    CreateJobRequest request;
    Empty response;
    grpc::ClientContext context;

    request.mutable_job()->set_id(2);
    request.mutable_job()->set_name("foo");
    request.mutable_job()->set_uid(1000);
    request.mutable_job()->set_gid(1000);
    request.mutable_job()->set_comm_pattern("test");
    request.mutable_job()->set_n_tasks(10);
    request.mutable_job()->set_state(JOB_RUNNING);

    auto status = stub->CreateJob(&context, request, &response);

    if (status.ok()) {
        std::cout << "ok!" << std::endl;
    } else {
        std::cout << "ng!" << std::endl;
    }

    return 0;
}
