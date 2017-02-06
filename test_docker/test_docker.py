# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import six

from docker import errors
from oslo_utils import timeutils
import driver
import utils as docker_utils

class DockerDriver(driver.ContainerDriver):
    '''Implementation of container drivers for Docker.'''

    def __init__(self):
        super(DockerDriver, self).__init__()

    def inspect_image(self, image, image_path=None):
        with docker_utils.docker_client() as docker:
            if image_path:
                with open(image_path, 'r') as fd:
                    docker.load_image(fd.read())
            image_dict = docker.inspect_image(image)
            return image_dict

    def images(self, repo, quiet=False):
        with docker_utils.docker_client() as docker:
            response = docker.images(repo, quiet)
            return response

    def create(self, context, container, sandbox_id, image):
        with docker_utils.docker_client() as docker:
            name = container.name
            if image['path']:
                with open(image['path'], 'r') as fd:
                    docker.load_image(fd.read())
            image = container.image

            kwargs = {
                'name': self.get_container_name(container),
                'command': container.command,
                'environment': container.environment,
                'working_dir': container.workdir,
                'labels': container.labels,
                'tty': container.tty,
                'stdin_open': container.stdin_open,
            }

            host_config = {}
            host_config['network_mode'] = 'container:%s' % sandbox_id
            # TODO(hongbin): Uncomment this after docker-py add support for
            # container mode for pid namespace.
            # host_config['pid_mode'] = 'container:%s' % sandbox_id
            host_config['ipc_mode'] = 'container:%s' % sandbox_id
            host_config['volumes_from'] = sandbox_id
            if container.memory is not None:
                host_config['mem_limit'] = container.memory
            if container.cpu is not None:
                host_config['cpu_quota'] = int(100000 * container.cpu)
                host_config['cpu_period'] = 100000
            if container.restart_policy is not None:
                count = int(container.restart_policy['MaximumRetryCount'])
                name = container.restart_policy['Name']
                host_config['restart_policy'] = {'Name': name,
                                                 'MaximumRetryCount': count}
            kwargs['host_config'] = docker.create_host_config(**host_config)

            response = docker.create_container(image, **kwargs)
            container.container_id = response['Id']
            container.status = fields.ContainerStatus.STOPPED
            container.save(context)
            return container

    def delete(self, container, force):
        with docker_utils.docker_client() as docker:
            if container.container_id:
                try:
                    docker.remove_container(container.container_id,
                                            force=force)
                except errors.APIError as api_error:
                    if '404' in str(api_error):
                        return
                    raise

    def list(self):
        with docker_utils.docker_client() as docker:
            return docker.list_instances()

    def show(self, container):
        with docker_utils.docker_client() as docker:
            if container.container_id is None:
                return container

            response = None
            try:
                response = docker.inspect_container(container.container_id)
            except errors.APIError as api_error:
                if '404' in str(api_error):
                    container.status = fields.ContainerStatus.ERROR
                    return container
                raise

            self._populate_container(container, response)
            return container

    def format_status_detail(self, status_time):
        try:
            st = datetime.datetime.strptime((status_time[:-4]),
                                            '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError as e:
            return
        delta = timeutils.utcnow() - st
        time_dict = {}
        time_dict['days'] = delta.days
        time_dict['hours'] = delta.seconds//3600
        time_dict['minutes'] = (delta.seconds % 3600)//60
        time_dict['seconds'] = delta.seconds
        if time_dict['days']:
            return '{} days'.format(time_dict['days'])
        if time_dict['hours']:
            return '{} hours'.format(time_dict['hours'])
        if time_dict['minutes']:
            return '{} mins'.format(time_dict['minutes'])
        if time_dict['seconds']:
            return '{} seconds'.format(time_dict['seconds'])
        return

    def _populate_container(self, container, response):
        status = response.get('State')
        if status:
            status_detail = ''
            if status.get('Error') is True:
                container.status = fields.ContainerStatus.ERROR
                status_detail = self.format_status_detail(
                    status.get('FinishedAt'))
                container.status_detail = "Exited({}) {} ago " \
                    "(error)".format(status.get('ExitCode'), status_detail)
            elif status.get('Paused'):
                container.status = fields.ContainerStatus.PAUSED
                status_detail = self.format_status_detail(
                    status.get('StartedAt'))
                container.status_detail = "Up {} (paused)".format(
                    status_detail)
            elif status.get('Running'):
                container.status = fields.ContainerStatus.RUNNING
                status_detail = self.format_status_detail(
                    status.get('StartedAt'))
                container.status_detail = "Up {}".format(
                    status_detail)
            else:
                container.status = fields.ContainerStatus.STOPPED
                status_detail = self.format_status_detail(
                    status.get('FinishedAt'))
                container.status_detail = "Exited({}) {} ago ".format(
                    status.get('ExitCode'), status_detail)
            if status_detail is None:
                container.status_detail = None

        config = response.get('Config')
        if config:
            self._populate_hostname_and_ports(container, config)

    def _populate_hostname_and_ports(self, container, config):
        # populate hostname
        container.hostname = config.get('Hostname')
        # populate ports
        ports = []
        exposed_ports = config.get('ExposedPorts')
        if exposed_ports:
            for key in exposed_ports:
                port = key.split('/')[0]
                ports.append(int(port))
        container.ports = ports

    def reboot(self, container, timeout):
        with docker_utils.docker_client() as docker:
            if timeout:
                docker.restart(container.container_id,
                               timeout=int(timeout))
            else:
                docker.restart(container.container_id)
            container.status = fields.ContainerStatus.RUNNING
            return container

    def stop(self, container, timeout):
        with docker_utils.docker_client() as docker:
            if timeout:
                docker.stop(container.container_id,
                            timeout=int(timeout))
            else:
                docker.stop(container.container_id)
            container.status = fields.ContainerStatus.STOPPED
            return container

    def start(self, container):
        with docker_utils.docker_client() as docker:
            docker.start(container.container_id)
            container.status = fields.ContainerStatus.RUNNING
            return container

    def pause(self, container):
        with docker_utils.docker_client() as docker:
            docker.pause(container.container_id)
            container.status = fields.ContainerStatus.PAUSED
            return container

    def unpause(self, container):
        with docker_utils.docker_client() as docker:
            docker.unpause(container.container_id)
            container.status = fields.ContainerStatus.RUNNING
            return container

    def show_logs(self, container):
        with docker_utils.docker_client() as docker:
            return docker.get_container_logs(container.container_id)

    def execute(self, container, command):
        with docker_utils.docker_client() as docker:
            create_res = docker.exec_create(
                container.container_id, command, True, True, False)
            exec_output = docker.exec_start(create_res, False, False, False)
            return exec_output

    def kill(self, container, signal=None):
        with docker_utils.docker_client() as docker:
            if signal is None or signal == 'None':
                docker.kill(container.container_id)
            else:
                docker.kill(container.container_id, signal)
            try:
                response = docker.inspect_container(container.container_id)
            except errors.APIError as api_error:
                if '404' in str(api_error):
                    container.status = fields.ContainerStatus.ERROR
                    return container
                raise

            self._populate_container(container, response)
            return container

    def update(self, container):
        patch = container.obj_get_changes()

        args = {}
        memory = patch.get('memory')
        if memory is not None:
            args['mem_limit'] = memory
        cpu = patch.get('cpu')
        if cpu is not None:
            args['cpu_quota'] = int(100000 * cpu)
            args['cpu_period'] = 100000

        with docker_utils.docker_client() as docker:
            try:
                resp = docker.update_container(container.container_id, **args)
                return resp
            except errors.APIError:
                raise

    def _encode_utf8(self, value):
        if six.PY2 and not isinstance(value, unicode):
            value = unicode(value)
        return value.encode('utf-8')

    def create_sandbox(self, context, container, image='kubernetes/pause'):
        with docker_utils.docker_client() as docker:
            name = self.get_sandbox_name(container)
            response = docker.create_container(image, name=name,
                                               hostname=name[:63])
            sandbox_id = response['Id']
            docker.start(sandbox_id)
            return sandbox_id

    def delete_sandbox(self, context, sandbox_id):
        with docker_utils.docker_client() as docker:
            try:
                docker.remove_container(sandbox_id, force=True)
            except errors.APIError as api_error:
                if '404' in str(api_error):
                    return
                raise

    def stop_sandbox(self, context, sandbox_id):
        with docker_utils.docker_client() as docker:
            docker.stop(sandbox_id)

    def get_sandbox_id(self, container):
        if container.meta:
            return container.meta.get('sandbox_id', None)
        else:
            return None

    def set_sandbox_id(self, container, sandbox_id):
        if container.meta is None:
            container.meta = {'sandbox_id': sandbox_id}
        else:
            container.meta['sandbox_id'] = sandbox_id

    def get_sandbox_name(self, container):
        return 'zun-sandbox-' + container.uuid

    def get_container_name(self, container):
        return 'zun-' + container.uuid

    def get_addresses(self, context, container):
        sandbox_id = self.get_sandbox_id(container)
        with docker_utils.docker_client() as docker:
            response = docker.inspect_container(sandbox_id)
            addr = response["NetworkSettings"]["IPAddress"]
            addresses = {
                'default': [
                    {
                        'addr': addr,
                    },
                ],
            }
            return addresses
