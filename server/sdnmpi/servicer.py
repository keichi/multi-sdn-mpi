from logging import getLogger

from . import sdnmpi_pb2, sdnmpi_pb2_grpc
from .models import Job, JobState, Process, ProcessState

logger = getLogger(__name__)


class SDNMPIServicer(sdnmpi_pb2_grpc.SDNMPIServicer):
    def ListJob(self, request, context):
        resp = sdnmpi_pb2.ListJobResponse()

        for job in Job.select():
            j = resp.jobs.add()

            j.id = job.id
            j.name = job.name
            j.uid = job.uid
            j.gid = job.gid
            j.comm_pattern = job.comm_pattern
            j.n_tasks = job.n_tasks
            j.state = job.state

        return resp

    def GetJob(self, request, context):
        job = Job.get_by_id_(request.id)

        response = sdnmpi_pb2.GetJobResponse()
        response.id = job.id
        response.name = job.name
        response.uid = job.uid
        response.gid = job.gid
        response.comm_pattern = job.comm_pattern
        response.n_tasks = job.n_tasks
        response.state = job.state

        return response

    def CreateJob(self, request, context):
        Job.create(
            id=request.job.id,
            name=request.job.name,
            uid=request.job.uid,
            gid=request.job.gid,
            comm_pattern=request.job.comm_pattern,
            n_tasks=request.job.n_tasks,
            state=request.job.state
        )

        logger.info("Job %d created (name: %s, n_tasks: %d)",
                    request.job.id, request.job.name, request.job.n_tasks)

        return sdnmpi_pb2.Empty()

    def StartJob(self, request, context):
        job = Job.get_by_id(request.id)
        job.state = JobState.RUNNING.value
        job.save()

        logger.info("Job %d started", request.id)

        return sdnmpi_pb2.Empty()

    def FinishJob(self, request, context):
        job = Job.get_by_id(request.id)
        job.state = JobState.COMPLETE.value
        job.save()

        logger.info("Job %d finished", request.id)

        return sdnmpi_pb2.Empty()

    def ListProcess(self, request, context):
        response = sdnmpi_pb2.ListProcessResponse()

        for process in Process.select().where(Process.job_id ==
                                              request.job_id):
            p = response.processes.add()

            p.job_id = process.job_id
            p.rank = process.rank
            p.node_id = process.node_id
            p.node_name = process.node_name
            p.state = process.state

        return response

    def GetProcess(self, request, context):
        process = Process.get(Process.job_id == request.job_id and
                              Process.rank == request.rank)

        response = sdnmpi_pb2.GetProcessResponse()

        response.process.job_id = process.job_id
        response.process.rank = process.rank
        response.process.node_id = process.node_id
        response.process.node_name = process.node_name
        response.process.state = process.state

        return response

    def CreateProcess(self, request, context):
        Process.create(
            job_id=request.process.job_id,
            rank=request.process.rank,
            node_id=request.process.node_id,
            node_name=request.process.node_name,
            state=request.process.state
        )

        logger.info("Process %d of job %d created (node id: %d, node name: %s)",
                    request.process.rank, request.process.job_id,
                    request.process.node_id, request.process.node_name)

        return sdnmpi_pb2.Empty()

    def StartProcess(self, request, context):
        process = Process.get(Process.job_id == request.job_id and
                              Process.rank == request.rank)
        process.state = ProcessState.RUNNING.value
        process.save()

        logger.info("Process %d of job %d started", request.rank,
                    request.job_id)

        return sdnmpi_pb2.Empty()

    def FinishProcess(self, request, context):
        process = Process.get(Process.job_id == request.job_id and
                              Process.rank == request.rank)
        process.state = ProcessState.COMPLETE.value
        process.save()

        logger.info("Process %d of job %d finished", request.rank,
                    request.job_id)

        return sdnmpi_pb2.Empty()
