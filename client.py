import socket
from threading import Thread
import time
global client_socket
name_input = input("Bitte gib deinen Namen ein: ")
client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 1339)
client_socket.connect(server_addr)
client_socket.send(bytes(name_input + " Has joined the chat", "utf-8"))

def send_messages():
    while True:
        client_socket.send(bytes(name_input + ": " + input(), "utf-8"))


def get_messages():
    while True:
        try:
            msg = client_socket.recv(1024)
            if msg == "":
                time.sleep(1)
            else:
                print(str(msg, "utf-8"))
        except:
            time.sleep(1)


get_Thread = Thread(target=get_messages)
get_Thread.start()
get_thread = Thread(target=send_messages)
get_thread.start()












