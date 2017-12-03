from subprocess import check_output
from pexpect import pxssh

class Bot:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.session = self.ssh_connect()

    def ssh_connect(self):
        try:
            controller = pxssh.pxssh()
            controller.login(self.host, self.username, self.password)
            return controller
        except Exception as e:
            print e

    def get_sys_info():
        self.ip = check_output("ifconfig eth0 | sed -n '2s/[^:]*:\([^ ]*\).*/\1/p'",
                          shell=True)
        self.user = check_output(["echo", "$(logname)"])
        print self.ip, self.user

    def send_sys_info():
        self.session.sendline(self.ip, self.user)
        self.session.prompt()
        return self.session.before
