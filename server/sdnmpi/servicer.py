from logging import getLogger

import networkx

from . import sdnmpi_pb2, sdnmpi_pb2_grpc
from .interconnect_manager import InterconnectManager
from .models import Job, JobState, Process, ProcessState, db

logger = getLogger(__name__)


class SDNMPIServicer(sdnmpi_pb2_grpc.SDNMPIServicer):
    def __init__(self):
        self.graph = networkx.read_graphml("milk.graphml")
        self.im = InterconnectManager(self.graph)

        self.im.startup()

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
            n_started=0,
            n_exited=0,
            state=request.job.state
        )

        logger.info("Job %d created (name: %s, n_tasks: %d, comm_pattern: %s)",
                    request.job.id, request.job.name, request.job.n_tasks,
                    request.job.comm_pattern)

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

        logger.info("Job %d completed", request.id)

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

        logger.info("Process %d of job %d created (node id: %d, node name: "
                    "%s)",
                    request.process.rank, request.process.job_id,
                    request.process.node_id, request.process.node_name)

        return sdnmpi_pb2.Empty()

    def _prepare_interconnect(self, job_id):
        logger.info("Preparing interconnect for job %d", job_id)

        job = Job.get_by_id(job_id)
        procs = Process.select().where(Process.job_id == job_id)

        # 通信パターンの読み込み
        # プロセス配置の取得
        # 経路割当計算
        # フローエントリ生成
        # フローエントリ送信

        # TODO ジョブとフローの対応関係を保存する必要あり (cookie?)
        # TODO ジョブとリンク負荷の対応関係を保存する必要あり

        logger.info("Prepared interconnect for job %d", job_id)

    def _cleanup_interconnect(self, job_id):
        logger.info("Cleaning up interconnect for job %d", job_id)
        logger.info("Cleaned up interconnect for job %d", job_id)

    def StartProcess(self, request, context):
        with db.atomic():
            process = Process.get(Process.job_id == request.job_id and
                                  Process.rank == request.rank)
            process.state = ProcessState.RUNNING.value
            process.save()

            Job.update(n_started=Job.n_started + 1) \
               .where(id == request.job_id) \
               .execute()

        job = Job.get_by_id(request.job_id)

        logger.info("Process %d of job %d started", request.rank,
                    request.job_id)

        if job.n_started == job.n_tasks:
            self._prepare_interconnect(request.job_id)

        return sdnmpi_pb2.Empty()

    def FinishProcess(self, request, context):
        with db.atomic():
            process = Process.get(Process.job_id == request.job_id and
                                  Process.rank == request.rank)
            process.state = ProcessState.COMPLETE.value
            process.save()

            Job.update(n_exited=Job.n_exited + 1) \
               .where(id == request.job_id) \
               .execute()

        job = Job.get_by_id(request.job_id)

        logger.info("Process %d of job %d exited", request.rank,
                    request.job_id)

        if job.n_exited == job.n_tasks:
            self._cleanup_interconnect(request.job_id)

        return sdnmpi_pb2.Empty()
