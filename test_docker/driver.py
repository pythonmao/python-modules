class ContainerDriver(object):
    '''Base class for container drivers.'''

    def create(self, context, container, sandbox_name=None):
        """Create a container."""
        raise NotImplementedError()

    def delete(self, container, force):
        """Delete a container."""
        raise NotImplementedError()

    def list(self):
        """List all containers."""
        raise NotImplementedError()

    def show(self, container):
        """Show the details of a container."""
        raise NotImplementedError()

    def reboot(self, container):
        """Reboot a container."""
        raise NotImplementedError()

    def stop(self, container):
        """Stop a container."""
        raise NotImplementedError()

    def start(self, container):
        """Start a container."""
        raise NotImplementedError()

    def pause(self, container):
        """Pause a container."""
        raise NotImplementedError()

    def unpause(self, container):
        """Pause a container."""
        raise NotImplementedError()

    def show_logs(self, container):
        """Show logs of a container."""
        raise NotImplementedError()

    def execute(self, container, command):
        """Execute a command in a running container."""
        raise NotImplementedError()

    def kill(self, container, signal):
        """kill signal to a container."""
        raise NotImplementedError()

    def create_sandbox(self, context, container, **kwargs):
        """Create a sandbox."""
        raise NotImplementedError()

    def delete_sandbox(self, context, sandbox_id):
        """Delete a sandbox."""
        raise NotImplementedError()

    # Note: This is not currently used, but
    # may be used later
    def stop_sandbox(self, context, sandbox_id):
        """Stop a sandbox."""
        raise NotImplementedError()

    def get_sandbox_id(self, container):
        """Retrieve sandbox ID."""
        raise NotImplementedError()

    def set_sandbox_id(self, container, sandbox_id):
        """Set sandbox ID."""
        raise NotImplementedError()

    def get_sandbox_name(self, container):
        """Retrieve sandbox name."""
        raise NotImplementedError()

    def get_container_name(self, container):
        """Retrieve sandbox name."""
        raise NotImplementedError()

    def get_addresses(self, context, container):
        """Retrieve IP addresses of the container."""

    def update(self, container):
        """Update a container."""
        raise NotImplementedError()
