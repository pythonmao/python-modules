import subprocess
import signal
from oslo_log import log

LOG = log.getLogger(__name__)


def _subprocess_setup():
    # Python installs a SIGPIPE handler by default. This is usually not what
    # non-Python subprocesses expect.
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)


def _subprocess_popen(args, stdin=None, stdout=None, stderr=None, shell=False,
                      env=None, preexec_fn=_subprocess_setup, close_fds=True):
    return subprocess.Popen(args, shell=shell, stdin=stdin, stdout=stdout,
                            stderr=stderr, preexec_fn=preexec_fn,
                            close_fds=close_fds, env=env)


class SSHClient(object):
    def __init__(self, host, user, passwd, script):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.script = script

    def exec_command(self, cmd):
        LOG.info("Exec command: %s", cmd)
        cmd = self.script + ' ' + self.host + ' ' + self.user \
              + ' ' + self.passwd + ' ' + '"' + cmd + '"'
        return _subprocess_popen(cmd, shell=True,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
