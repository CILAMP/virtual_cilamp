# coding: utf-8
import sys
import socket
from threading import Thread
from time import sleep
from random import randrange

PY2 = sys.version_info < (3, 0)


# Fill the 2<>3 gap
if PY2:
    ConnectionRefusedError = Exception
    ConnectionResetError = Exception


def makebytes(s):
    if PY2:
        return str(s)
    else:
        return bytes(s, 'utf8')


class FakeLamp(Thread):

    def __init__(self, host, port, lampid, command_handler, state_changed):
        super(FakeLamp, self).__init__()
        self.host = host
        self.port = port
        self.lampid = lampid
        self.daemon = True
        self.handle_command = command_handler
        self.state_changed = state_changed

    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_address = (self.host, self.port)
                self.state_changed('CONNECTING')
                print("Connecting to %s %d..." % (self.host, self.port))
                sock.connect(server_address)
                print("Connected, sending lamp id '%s'." % self.lampid)
                sock.sendall(makebytes(self.lampid + '\n'))
                print("Waiting for commands.")
                data = b''
                self.state_changed('IDLE')
                while True:
                    data += sock.recv(1)
                    if not data:
                        print("Connection refused by remote host.")
                        raise ConnectionRefusedError()
                    if b'\n' in data:
                        self.handle_command(data[:-1])
                        data = b''
            except KeyboardInterrupt:
                return
            except (ConnectionRefusedError, ConnectionResetError):
                self.state_changed('DISCONNECTED')
                print("Not connected right now. Retrying in 3-7 seconds.")
                sleep(randrange(3, 8))
            finally:
                print('Closing socket gracefully.')
                sock.close()
