#!/usr/bin/env python3
# Documentation: https://docs.python.org/3/library/socket.html
import socket, json, sqlite3, sys
sys.path.append("..")
import socket_utils
    
HOST = "127.0.0.1"         # The server's hostname or IP address.
PORT = 63000               # The port used by the server.
ADDRESS = (HOST, PORT)

def main():
    user = { "username": "seth", "password": "testing", "carid": "1"}
    login(user)

def login(user):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Connecting to {}...".format(ADDRESS))
        s.connect(ADDRESS)
        print("Connected.")

        print("Logging in as {}".format(user["username"]))
        socket_utils.sendJson(s, user)

        print("Waiting for Master Pi...")
        while(True):
            object = socket_utils.recvJson(s)
            if("authenticated" in object):
                print("Welcome")
                print()
                break
            else:
                print("Wrong Username or Password")
                print()
                break

# Execute program.
if __name__ == "__main__":
    main()
