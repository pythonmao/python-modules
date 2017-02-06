import contextlib
import six

import docker
from docker import client
from docker import errors
from docker import tls
from docker.utils import utils

@contextlib.contextmanager
def docker_client():
    client_kwargs = dict()
    try:
        yield DockerHTTPClient(
            'unix:///var/run/docker.sock',
            '1.12',
            60,
            **client_kwargs
        )
    except errors.APIError as e:
        raise 


class DockerHTTPClient(client.Client):
    def __init__(self, url,
                 ver,
                 timeout,
                 ca_cert=None,
                 client_key=None,
                 client_cert=None):

        ssl_config = False

        super(DockerHTTPClient, self).__init__(
            base_url=url,
            version=ver,
            timeout=timeout,
            tls=ssl_config
        )

    def list_instances(self, inspect=False):
        """List all containers."""
        res = []
        for container in self.containers(all=True):
            info = self.inspect_container(container['Id'])
            if not info:
                continue
            if inspect:
                res.append(info)
            else:
                res.append(info['Config'].get('Hostname'))
        return res

    def pause(self, container):
        """Pause a running container."""
        if isinstance(container, objects.Container):
            container = container.container_id
        super(DockerHTTPClient, self).pause(container)

    def unpause(self, container):
        """Unpause a paused container."""
        if isinstance(container, objects.Container):
            container = container.container_id
        super(DockerHTTPClient, self).unpause(container)

    def get_container_logs(self, docker_id):
        """Fetch the logs of a container."""
        return self.logs(docker_id)
