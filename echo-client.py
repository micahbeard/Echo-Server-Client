# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5000  # The port used by the server
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024).upper()

    print(f"Received {data}")

except:
    print("Error")