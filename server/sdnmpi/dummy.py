from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_0


class DummyController(app_manager.RyuApp):
        OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
