from itertools import product
from logging import getLogger

import networkx

import requests


RYU_API_URL = "http://localhost:8080"
MIN_PRIO = 32768

logger = getLogger(__name__)


class InterconnectManager:
    def __init__(self, graph):
        self.graph = graph
        self.hosts = [n for n, d in graph.nodes.items()
                      if d["typ"] == "host"]
        self.switches = [n for n, d in graph.nodes.items()
                         if d["typ"] == "switch"]

    def prepare_for_job(self, job_id, routing):
        cookie = job_id

        for (src, dst), path in routing.items():
            if src == dst:
                continue

            src_mac = self._get_mac(src)
            dst_mac = self._get_mac(dst)

            for u, v in zip(path[1:-1], path[2:]):
                dpid = self._get_dpid(u)
                out_port = self._get_port(u, v)

                self._install_unicast_flow(dpid, src_mac, dst_mac, out_port,
                                           cookie=cookie,
                                           priority=MIN_PRIO + 100)

    def cleanup_for_job(self, job_id):
        cookie = job_id

        for switch in self.switches:
            dpid = self._get_dpid(switch)

            self._query_flow_stats(dpid, cookie)
            self._remove_unicast_flows(dpid, cookie)

    def startup(self):
        # Clear flow tables
        for switch in self.switches:
            dpid = self._get_dpid(switch)
            self._clear_flows(dpid)
        logger.info("Cleared flow tables")

        addrs = {host: i for i, host in enumerate(self.hosts)}

        # Install flows for all host pairs
        for (src, dst) in product(self.hosts, self.hosts):
            if src == dst:
                continue

            path = networkx.shortest_path(self.graph, src, dst)

            paths = list(networkx.all_shortest_paths(self.graph, src, dst))
            indices = list(range(len(paths)))

            for i in range(len(paths[0])):
                # Path decided
                if len(indices) == 1:
                    break

                switches = sorted(list({paths[j][i] for j in indices}))

                # Only single option, skipping to next switch in path
                if len(switches) == 1:
                    continue

                switch = switches[addrs[dst] % len(switches)]

                indices = [j for j in indices if paths[j][i] == switch]

            path = paths[indices.pop()]

            src_mac = self._get_mac(src)
            dst_mac = self._get_mac(dst)

            for u, v in zip(path[1:-1], path[2:]):
                dpid = self._get_dpid(u)
                out_port = self._get_port(u, v)

                self._install_unicast_flow(dpid, src_mac, dst_mac, out_port)
        logger.info("Installed default flows for all host pairs")

        # Install flooding flows for broadcast packets
        for switch in self.switches:
            dpid = self._get_dpid(switch)
            self._install_bcast_flow(dpid)
        logger.info("Installed flows for flooding bcast packets")

        # Compute links that must be blocked to remove loops
        g = networkx.Graph(self.graph)
        mst = networkx.minimum_spanning_tree(g)
        diff = networkx.difference(g, mst)

        # Block links
        for u, v in diff.edges:
            dpid = self._get_dpid(u)
            port = out_port = self._get_port(u, v)

            self._install_bcast_block_flow(dpid, port)

            dpid = self._get_dpid(v)
            port = self._get_port(v, u)

            self._install_bcast_block_flow(dpid, port)
        logger.info("Installed flows for removing loops")

    def _clear_flows(self, dpid):
        requests.delete(RYU_API_URL + "/stats/flowentry/clear/" + str(dpid))

    def _query_flow_stats(self, dpid, cookie):
        r = requests.post(RYU_API_URL + "/stats/flow/" + str(dpid))

        packet_count = 0
        byte_count = 0
        flow_count = 0

        for stats in r.json()[str(dpid)]:
            if stats["cookie"] != cookie:
                continue

            packet_count += stats["packet_count"]
            byte_count += stats["byte_count"]
            flow_count += 1

        logger.info("Job %d consumed %d packets, %d bytes, %d flows"
                    " on datapath %d", cookie, packet_count, byte_count,
                    flow_count, dpid)

    def _remove_unicast_flows(self, dpid, cookie):
        payload = {
            "dpid": dpid,
            "cookie": cookie
        }
        r = requests.post(RYU_API_URL + "/stats/flowentry/delete_strict",
                          json=payload)
        r.raise_for_status()

    def _install_unicast_flow(self, dpid, src_mac, dst_mac, out_port,
                              cookie=None, priority=MIN_PRIO):
        payload = {
            "dpid": dpid,
            "match": {
                "dl_src": src_mac,
                "dl_dst": dst_mac,
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "port": out_port
                }
            ]
        }

        if cookie:
            payload["cookie"] = cookie

        if priority:
            payload["priority"] = priority

        r = requests.post(RYU_API_URL + "/stats/flowentry/add", json=payload)
        r.raise_for_status()

    def _install_bcast_flow(self, dpid):
        payload = {
            "dpid": dpid,
            "match": {
                "dl_dst": "ff:ff:ff:ff:ff:ff",
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "port": "FLOOD"
                }
            ]
        }

        r = requests.post(RYU_API_URL + "/stats/flowentry/add", json=payload)
        r.raise_for_status()

    def _install_bcast_block_flow(self, dpid, in_port):
        payload = {
            "dpid": dpid,
            "match": {
                "in_port": in_port,
                "dl_dst": "ff:ff:ff:ff:ff:ff",
            },
            "actions": []
        }

        r = requests.post(RYU_API_URL + "/stats/flowentry/add", json=payload)
        r.raise_for_status()

    def _get_dpid(self, switch):
        return self.graph.nodes[switch]["dpid"]

    def _get_mac(self, host):
        return self.graph.nodes[host]["mac"]

    def _get_port(self, src, dst):
        return self.graph.edges[src, dst]["port"]
