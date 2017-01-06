#!/usr/bin/python
# network mapper docker / openvwitch
from pyroute2 import IPDB

import ovs_adapter.neutron.ovs_lib as ovs_lib


##api for docker
class OVSAdapter(object):
    def __init__(self):
        self.ovs = ovs_lib.BaseOVS()
        self.ipdb = IPDB()

    def get_all_eths(self):
        return self.ipdb.by_name.keys()

    def get_eth_by_name(self, name):
        return self.ipdb.by_name.get(name, None)

    def create_veth(self, ifname, kind, peer=None):
        # create veth interface
        self.ipdb.create(ifname=ifname, kind=kind, peer=peer).commit()
        return (ifname, peer)

    def del_veth(self, eth):
        self.ipdb.interfaces[eth].remove().commit()

    def add_ip(self, eth, ip=None):
        if ip:
            self.ipdb.interfaces[eth].add_ip(ip)
        self.ipdb.interfaces[eth].up().commit()
        return ip

    def add_route(self, dst, gateway):
        self.ipdb.routes.add({'dst': dst, 'gateway': gateway}).commit()

    def eth_up(self, eth):
        self.ipdb.interfaces[eth].up().commit()

    def eth_down(self, eth):
        self.ipdb.interfaces[eth].down().commit()

    def get_bridge_by_port(self, eth):
        for br in self.ovs.get_bridges():
            if eth in self.ovs.add_bridge(br).get_port_name_list():
                return br

    def add_port(self, br, eth):
        if br not in self.ovs.get_bridges():
            return 'failed'
        self.ovs.add_bridge(br).add_port(eth)
        return 'success'

    def del_port(self, br, eth):
        if br not in self.ovs.get_bridges():
            return 'failed'
        self.ovs.add_bridge(br).delete_port(eth)
        return 'success'