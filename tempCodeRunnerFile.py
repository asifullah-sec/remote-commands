from socket import socket, AF_INET,SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as socket_server:
    socket_server.bind(("0.0.0.0",8888))
    socket_server.listen()


    while True:
        client_socket,client_address=socket_server.accept()
        print(client_socket.recv(1024).decode(),client_address)
        client_socket.sendall(b"connected")