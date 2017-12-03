import sys
from pexpect import pxssh

class Controller:
    def __init__(self):
        self.bots = []

    def send_command(self, command):
        for bot in self.bots:
            self.session.sendline(command)
            self.session.prompt()
            return self.session.before

    def get_clients(self):
        with open('bots', 'r') as bots_file:
            self.bots.append(bots_file.readline())


if __name__ == "__main__":
    me = Controller()
    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "command"
    else:
        me.send_command(sys.argv[1])

