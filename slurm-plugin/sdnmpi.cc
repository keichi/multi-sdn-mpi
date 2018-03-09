#include <cstdlib>
#include <string>

#include <grpc++/grpc++.h>
#include "sdnmpi.grpc.pb.h"

extern "C" {

#include <slurm/spank.h>

int slurm_spank_local_user_init(spank_t spank, int argc, char *argv[])
{
    if (spank_context() != S_CTX_LOCAL) {
        return ESPANK_SUCCESS;
    }

    uint32_t job_id, uid, gid, n_tasks;
    spank_get_item(spank, S_JOB_ID, &job_id);
    spank_get_item(spank, S_JOB_UID, &uid);
    spank_get_item(spank, S_JOB_GID, &gid);
    spank_get_item(spank, S_JOB_TOTAL_TASK_COUNT, &n_tasks);

    char *job_name;
    job_name = std::getenv("SLURM_JOB_NAME");

    const auto cred = grpc::InsecureChannelCredentials();
    const auto chan = grpc::CreateChannel("192.168.69.100:50051", cred);
    const auto stub = SDNMPI::NewStub(chan);

    {
        grpc::ClientContext context;
        CreateJobRequest request;
        Empty response;

        Job *job = request.mutable_job();
        job->set_id(job_id);
        job->set_name(job_name);
        job->set_uid(uid);
        job->set_gid(gid);
        job->set_n_tasks(n_tasks);
        job->set_state(JOB_PENDING);

        stub->CreateJob(&context, request, &response);
    }

    {
        grpc::ClientContext context;
        StartJobRequest request;
        Empty response;

        request.set_id(job_id);

        stub->StartJob(&context, request, &response);
    }

    return ESPANK_SUCCESS;
}

int slurm_spank_exit(spank_t spank, int argc, char *argv[])
{
    if (spank_context() != S_CTX_LOCAL) {
        return ESPANK_SUCCESS;
    }

    char *job_id;
    job_id = std::getenv("SLURM_JOB_ID");

    const auto cred = grpc::InsecureChannelCredentials();
    const auto chan = grpc::CreateChannel("192.168.69.100:50051", cred);
    const auto stub = SDNMPI::NewStub(chan);

    {
        grpc::ClientContext context;
        FinishJobRequest request;
        Empty response;

        if (job_id != NULL) {
            request.set_id(std::stoi(job_id));
        }

        stub->FinishJob(&context, request, &response);
    }

    return ESPANK_SUCCESS;
}

}
