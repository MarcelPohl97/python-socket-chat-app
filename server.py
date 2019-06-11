import socket
from threading import Thread

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 1339))
server_socket.listen(2)

def handle_chat():
    global client_socket, addr
    while True:
        client_socket, addr = server_socket.accept()
        client_socket.send(bytes("Welcome to the Chat App", "utf-8"))
        Thread(target=get_message).start()



def get_message():
    global message, addr, client_socket
    while True:
        name = client_socket.recv(1024)
        print(str(name, "utf-8"))
        while True:
            msg = client_socket.recv(1024)
            print(str(msg, "utf-8"))
            client_socket.send(msg)




Accept_Thread = Thread(target=handle_chat)
Accept_Thread.start()










