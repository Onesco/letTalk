from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
from client_objects import Person

# Global CONSTANTS
HOST = "localhost"
PORT = 3200
ADDR = (HOST, PORT)
MAX_CONNECTION = 5
BUFSIZE = 512

# create server
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

# GLOBAL VARIABLES
persons = []

# multi-tread application
#    concurrent thread.
# 1. thread waiting for your connections
# 2. thread waiting for messages
# 3. thread send outcome data to client

def broadcast(msg, name):
    """"
    send message to all clients
    :param:msg: bytes['utf8']
    :param:name:str
    :return:None
    """
    for person in persons:
        client = person.client
        client.send(bytes(name, "utf8") + msg)

def client_communication(person):
    """"
    wait for connection from new client, start new thread was connceted
    :param: person: Person
    :return: None
    """
    client = person.client
    name = client.recv(BUFSIZE).decode('utf8')
    person.set_name(name)
    msg = bytes(f'{name} has joined the chat','utf8')

    broadcast(msg, "")  # broadcast welcome message
    isConnected = True
    while isConnected:
        try:
            msg = client.recv(BUFSIZE)
            if msg == bytes("{quit}", "utf8"):
                client.close()
                print(f'[DISCONNECTED] {person.name} has left')
                persons.remove(person)
                broadcast(bytes(f'{person.name} has left the chat','utf8'), '')
                # client.send(bytes("{quit}", "utf8"))
                break
            else:
                broadcast(msg, person.name+":")
                print(f'{person.name}:', msg.decode('utf8'))
        except Exception as error:
            print(f'[EXCEPTION] failed to broadcast client communication', error)
            break

def accept_incoming_connections():
    """"
    wait for connection from new client, start new thread was connceted
    :param: None
    :return: None
    """
    is_running = True
    while is_running:
        try:
            client, address = SERVER.accept()
            person = Person(address, client)  # create a person object for the client
            persons.append(person)
            print(f"[CONNECTED] {address} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as error:
            print('[EXCEPTION]', error)
            is_running = False


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTION)  # listening for connection
    print('[STARTED] waiting for connection ...')
    ACCEPT_TREAD = Thread(target=accept_incoming_connections)
    ACCEPT_TREAD.start()
    ACCEPT_TREAD.join()
    SERVER.close()
