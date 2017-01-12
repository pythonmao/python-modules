#!/usr/bin/python
# network mapper docker / openvwitch
from pyroute2 import IPDB

# need file neutron/agent/common/ovs_lib.py
from backend.server.openvswitch.neutron import ovs_lib


##api for docker
class OVSAdapter(object):
    def __init__(self):
        self.ovs_adapter = ovs_lib.BaseOVS()

    def add_bridge(self, bridge):
        return self.ovs_adapter.add_bridge(bridge)

    def del_bridge(self, bridge):
        return self.ovs_adapter.delete_bridge(bridge)

    def get_all_bridges(self):
        return self.ovs_adapter.get_bridges()

    def get_port_list(self, bridge):
        # get the port name list for this bridge
        return self.ovs_adapter.ovsdb.list_ports(bridge).execute(check_error=True)

    def port_exists(self, port):
        return self.ovs_adapter.port_exists(port)

    def bridge_exists(self, bridge):
        return self.ovs_adapter.bridge_exists(bridge)

    def get_bridge_by_port(self, port):
        for br in self.get_all_bridges():
            if port in self.get_port_list(br):
                return br

    def add_port(self, bridge, port, *interface_attr_tuples):
        if not self.bridge_exists(bridge) or self.port_exists(port):
            return 'failed'
        with self.ovs_adapter.ovsdb.transaction() as txn:
            txn.add(self.ovs_adapter.ovsdb.add_port(bridge, port))
            if interface_attr_tuples:
                txn.add(self.ovs_adapter.ovsdb.db_set('Interface', port,
                                                      *interface_attr_tuples))
        return 'success'
        # return self.get_port_ofport(port)

    def del_port(self, bridge, port):
        if not self.bridge_exists(bridge) or not self.port_exists(port):
            return 'failed'
        self.ovs_adapter.ovsdb.delete_port(port)
        return 'success'


class NetworkAdapter(object):
    def __init__(self):
        self.ipdb = IPDB()

    def get_all_eths(self):
        return self.ipdb.interfaces.keys()

    def get_eth_by_name(self, name):
        return self.ipdb.interfaces.get(name, None)

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
    
    def add_port(self, bridge, port):
        self.ipdb.interfaces[bridge].add_port(port).commit()
        return port

    def add_route(self, dst, gateway):
        self.ipdb.routes.add({'dst': dst, 'gateway': gateway}).commit()

    def eth_up(self, eth):
        self.ipdb.interfaces[eth].up().commit()

    def eth_down(self, eth):
        self.ipdb.interfaces[eth].down().commit()
