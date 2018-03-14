from itertools import product
from logging import getLogger
import math

import networkx

from . import sdnmpi_pb2, sdnmpi_pb2_grpc
from .interconnect_manager import InterconnectManager
from .models import CommPair, CommPattern, Job, JobState, Process,\
    ProcessState, db

logger = getLogger(__name__)


class SDNMPIServicer(sdnmpi_pb2_grpc.SDNMPIServicer):
    def __init__(self):
        self.graph = networkx.read_graphml("milk.graphml")

        for u, v in self.graph.edges:
            self.graph.edges[u, v]["traffic"] = 0
            self.graph.edges[u, v]["alloc"] = {}

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

        logger.debug("Process %d of job %d created (node id: %d, node name: "
                     "%s)",
                     request.process.rank, request.process.job_id,
                     request.process.node_id, request.process.node_name)

        return sdnmpi_pb2.Empty()

    def _compute_routing_greedy(self, job, pattern):
        mapping = {}
        for proc in job.processes:
            mapping[proc.rank] = proc.node_name

        routing = {}
        for pair in pattern.pairs.order_by(CommPair.tx_bytes):
            src = mapping[pair.src]
            dst = mapping[pair.dst]

            if (src, dst) in routing:
                path = routing[src, dst]
            else:
                paths = list(networkx.all_shortest_paths(self.graph, src, dst))
                min_path = paths[0]
                min_cost = math.inf

                for path in paths:
                    cost = 0

                    for u, v in zip(path[:-1], path[1:]):
                        cost += self.graph.edges[u, v]["traffic"]

                    if cost < min_cost:
                        min_path = path
                        min_cost = cost

                path = min_path
                routing[src, dst] = path

            for u, v in zip(path[1:-1], path[2:-1]):
                self.graph.edges[u, v]["traffic"] += pair.tx_bytes
                self.graph.edges[u, v]["alloc"][job.id] = pair.tx_bytes

        return routing

    def _prepare_interconnect(self, job):
        logger.info("Preparing interconnect for job %d", job.id)

        pattern = CommPattern.get_or_none(CommPattern.name == job.comm_pattern)
        if not pattern:
            logger.info("Skipping reconfiguration for job %d since"
                        " communication pattern is unknown", job.id)
            return

        routing = self._compute_routing_greedy(job, pattern)
        self.im.prepare_for_job(job.id, routing)

        logger.info("Prepared interconnect for job %d", job.id)

    def _cleanup_interconnect(self, job):
        logger.info("Cleaning up interconnect for job %d", job.id)

        for u, v, alloc in self.graph.edges.data("alloc", default={}):
            if job.id not in alloc:
                continue

            self.graph.edges[u, v]["traffic"] -= alloc[job.id]

        self.im.cleanup_for_job(job.id)

        logger.info("Cleaned up interconnect for job %d", job.id)

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

        logger.debug("Process %d of job %d started", request.rank,
                     request.job_id)

        if job.n_started == job.n_tasks:
            self._prepare_interconnect(job)

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

        logger.debug("Process %d of job %d exited", request.rank,
                     request.job_id)

        if job.n_exited == job.n_tasks:
            self._cleanup_interconnect(job)

        return sdnmpi_pb2.Empty()
