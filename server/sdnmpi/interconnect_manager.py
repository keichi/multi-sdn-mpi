from itertools import product
from logging import getLogger

import networkx

import requests


RYU_API_URL = "http://localhost:8080"

logger = getLogger(__name__)


class InterconnectManager:
    def __init__(self, graph):
        self.graph = graph
        self.hosts = [n for n, d in graph.nodes.items()
                      if d["typ"] == "host"]
        self.switches = [n for n, d in graph.nodes.items()
                         if d["typ"] == "switch"]

    def startup(self):
        # Clear flow tables
        for switch in self.switches:
            dpid = self._get_dpid(switch)
            self._clear_flows(dpid)
        logger.info("Cleared flow tables")

        # Install flows for all host pairs
        for (src, dst) in product(self.hosts, self.hosts):
            if src == dst:
                continue

            path = networkx.shortest_path(self.graph, src, dst)
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
        logger.info("Installed flooding flows")

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
        logger.info("Installed drop flows for removing loops")

    def _clear_flows(self, dpid):
        requests.delete(RYU_API_URL + "/stats/flowentry/clear/" + str(dpid))

    def _install_unicast_flow(self, dpid, src_mac, dst_mac, out_port):
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

        requests.post(RYU_API_URL + "/stats/flowentry/add", json=payload)

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

        requests.post(RYU_API_URL + "/stats/flowentry/add", json=payload)

    def _install_bcast_block_flow(self, dpid, in_port):
        payload = {
            "dpid": dpid,
            "match": {
                "in_port": in_port,
                "dl_dst": "ff:ff:ff:ff:ff:ff",
            },
            "actions": []
        }

        requests.post(RYU_API_URL + "/stats/flowentry/add", json=payload)

    def _get_dpid(self, switch):
        return self.graph.nodes[switch]["dpid"]

    def _get_mac(self, host):
        return self.graph.nodes[host]["mac"]

    def _get_port(self, src, dst):
        return self.graph.edges[src, dst]["port"]
