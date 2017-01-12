# Copyright 2011 VMware, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from backend.server.openvswitch.neutron import api as ovsdb


class BaseOVS(object):

    def __init__(self):
        self.ovsdb = ovsdb.API.get(self)

    def add_manager(self, connection_uri):
        self.ovsdb.add_manager(connection_uri).execute()

    def get_manager(self):
        return self.ovsdb.get_manager().execute()

    def remove_manager(self, connection_uri):
        self.ovsdb.remove_manager(connection_uri).execute()

    def add_bridge(self, bridge_name,
                   datapath_type='system'):

        self.ovsdb.add_br(bridge_name,
                          datapath_type).execute()
        return bridge_name

    def delete_bridge(self, bridge_name):
        self.ovsdb.del_br(bridge_name).execute()

    def bridge_exists(self, bridge_name):
        return self.ovsdb.br_exists(bridge_name).execute()

    def port_exists(self, port_name):
        cmd = self.ovsdb.db_get('Port', port_name, 'name')
        return bool(cmd.execute(check_error=False, log_errors=False))

    def get_bridge_for_iface(self, iface):
        return self.ovsdb.iface_to_br(iface).execute()

    def get_bridges(self):
        return self.ovsdb.list_br().execute(check_error=True)

    def get_bridge_external_bridge_id(self, bridge):
        return self.ovsdb.br_get_external_id(bridge, 'bridge-id').execute()

    def set_db_attribute(self, table_name, record, column, value,
                         check_error=False, log_errors=True):
        self.ovsdb.db_set(table_name, record, (column, value)).execute(
            check_error=check_error, log_errors=log_errors)

    def clear_db_attribute(self, table_name, record, column):
        self.ovsdb.db_clear(table_name, record, column).execute()

    def db_get_val(self, table, record, column, check_error=False,
                   log_errors=True):
        return self.ovsdb.db_get(table, record, column).execute(
            check_error=check_error, log_errors=log_errors)

    @property
    def config(self):
        """A dict containing the only row from the root Open_vSwitch table
        This row contains several columns describing the Open vSwitch install
        and the system on which it is installed. Useful keys include:
            datapath_types: a list of supported datapath types
            iface_types: a list of supported interface types
            ovs_version: the OVS version
        """
        return self.ovsdb.db_list("Open_vSwitch").execute()[0]

