#include <cstdlib>
#include <string>

#include <unistd.h>

#include <grpc++/grpc++.h>
#include "sdnmpi.grpc.pb.h"

extern "C" {

// Below macro definitions are taken from slurm/slurm.h
/* Job step ID of external process container */
#define SLURM_PENDING_STEP (0xfffffffd)
/* Job step ID of batch scripts */
#define SLURM_BATCH_SCRIPT (0xfffffffe)
/* Job step ID of external process container */
#define SLURM_EXTERN_CONT  (0xffffffff)

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

int slurm_spank_task_init(spank_t spank, int argc, char *argv[])
{
    if (!spank_remote(spank)) {
        return ESPANK_SUCCESS;
    }

    const auto cred = grpc::InsecureChannelCredentials();
    const auto chan = grpc::CreateChannel("192.168.69.100:50051", cred);
    const auto stub = SDNMPI::NewStub(chan);

    uint32_t job_id, job_step_id, rank, node_id;
    spank_get_item(spank, S_JOB_ID, &job_id);
    spank_get_item(spank, S_JOB_STEPID, &job_step_id);
    spank_get_item(spank, S_TASK_GLOBAL_ID, &rank);
    spank_get_item(spank, S_JOB_NODEID, &node_id);

    if (job_step_id == SLURM_PENDING_STEP \
        || job_step_id == SLURM_BATCH_SCRIPT \
        || job_step_id == SLURM_EXTERN_CONT) {
        return ESPANK_SUCCESS;
    }

    char node_name[HOST_NAME_MAX];
    gethostname(node_name, HOST_NAME_MAX);

    {
        grpc::ClientContext context;
        CreateProcessRequest request;
        Empty response;

        Process *process = request.mutable_process();

        process->set_job_id(job_id);
        process->set_rank(rank);
        process->set_node_id(node_id);
        process->set_node_name(node_name);
        process->set_state(PROCESS_PENDING);

        stub->CreateProcess(&context, request, &response);
    }

    {
        grpc::ClientContext context;
        StartProcessRequest request;
        Empty response;

        request.set_job_id(job_id);
        request.set_rank(rank);

        stub->StartProcess(&context, request, &response);
    }

}

int slurm_spank_task_exit(spank_t spank, int argc, char *argv[])
{
    if (!spank_remote(spank)) {
        return ESPANK_SUCCESS;
    }

    const auto cred = grpc::InsecureChannelCredentials();
    const auto chan = grpc::CreateChannel("192.168.69.100:50051", cred);
    const auto stub = SDNMPI::NewStub(chan);

    uint32_t job_id, rank;
    spank_get_item(spank, S_JOB_ID, &job_id);
    spank_get_item(spank, S_TASK_GLOBAL_ID, &rank);

    {
        grpc::ClientContext context;
        FinishProcessRequest request;
        Empty response;

        request.set_job_id(job_id);
        request.set_rank(rank);

        stub->FinishProcess(&context, request, &response);
    }

}

}
