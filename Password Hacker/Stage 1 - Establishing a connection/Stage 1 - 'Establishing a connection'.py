import socket
import sys

args = sys.argv
with socket.socket() as client_socket:
    hostname = args[1]
    port = args[2]
    message = args[3]
    address = (hostname, int(port))
    client_socket.connect(address)
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(response.decode())