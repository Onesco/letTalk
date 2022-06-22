from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
# Global CONSTANTS
HOST = "localhost"
PORT = 3200
ADDR = (HOST, PORT)
BUFSIZE = 512

# Global VARIABLE
messages = []
# create server
CLIENT_SOCKET= socket(AF_INET, SOCK_STREAM)
CLIENT_SOCKET.connect(ADDR)

def send_message(msg):
    CLIENT_SOCKET.send(bytes(msg, 'utf8'))
    if msg == 'quit':
        CLIENT_SOCKET.close()

def receive_message():
    while True:
        try:
            msg = CLIENT_SOCKET.recv(BUFSIZE).decode()
            messages.append(msg)
            print(msg)
        except Exception as error:
            print('[EXCEPTION]', error)
            break

receive_thread = Thread(target=receive_message)
receive_thread.start()

send_message("Onesco")
time.sleep(0.1)
send_message("good evening guys")
time.sleep(0.1)
send_message("how far")
time.sleep(2)
send_message("{quit}")