import paramiko
import six


class SSHClient(object):
    def __init__(self, host, user, password, port=None, key_contents=None,
                 key_filename=None, timeout=None):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.host = host
            if key_contents:
                data = six.StringIO(key_contents)
                if "BEGIN RSA PRIVATE" in key_contents:
                    pkey = paramiko.RSAKey.from_private_key(data)
                elif "BEGIN DSA PRIVATE" in key_contents:
                    pkey = paramiko.DSSKey.from_private_key(data)
                else:
                    # Can't include the key contents - secure material.
                    raise ValueError("Invalid private key")
            else:
                pkey = None
            self.ssh.connect(host,
                             username=user,
                             password=password,
                             port=port if port else 22,
                             pkey=pkey,
                             key_filename=key_filename if not pkey else None,
                             timeout=timeout if timeout else 0)
        except Exception as e:
            print 'error'

    def close(self):
        if self.ssh:
            self.ssh.close()

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        if stderr:
            print 'command error'

        return stdout

ssh = SSHClient('10.240.198.57', 'root', 'Passw0rd')
ssh.exec_command('ls /')
