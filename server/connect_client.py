from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Client:
    def __init__(self, name):
        # Global CONSTANTS
        self.HOST = "localhost"
        self.PORT = 3200
        self.ADDR = (self.HOST, self.PORT)
        self.BUFSIZE = 512

        # Global VARIABLE
        self.messages = []
        self.name = name
        # create server
        self.CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
        self.CLIENT_SOCKET.connect(self.ADDR)

        receive_thread = Thread(target=self.receive_message)
        receive_thread.start()

        self.send_message(name)

    def send_message(self,msg):
        self.CLIENT_SOCKET.send(bytes(msg, 'utf8'))
        if msg == 'quit':
            self.CLIENT_SOCKET.close()

    def receive_message(self):
        while True:
            try:
                msg = self.CLIENT_SOCKET.recv(self.BUFSIZE).decode()
                self.messages.append(msg)
                print(msg)
            except Exception as error:
                print('[EXCEPTION]', error)
                break



