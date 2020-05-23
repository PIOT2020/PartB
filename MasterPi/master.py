#!/usr/bin/env python3
# Documentation: https://docs.python.org/3/library/socket.html
import socket, json, sys
sys.path.append("..")
import socket_utils

HOST = ""    # Empty string means to listen on all IP's on the machine, also works with IPv6.
             # Note "0.0.0.0" also works but only with IPv4.
PORT = 63000 # Port to listen on (non-privileged ports are > 1023).
ADDRESS = (HOST, PORT)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDRESS)
        s.listen()

        print("Listening on {}...".format(ADDRESS))
        while True:
            print("Waiting for Agent Pi...")
            conn, addr = s.accept()
            with conn:
                print("Connected to {}".format(addr))
                print()

                user = socket_utils.recvJson(conn)
    
                
                if (user["username"] == "seth" and user["password"] == "testing"):
                    socket_utils.sendJson(conn, { "authenticated": True })
                else:
                    socket_utils.sendJson(conn, { "authenticated": False })


# Execute program.
if __name__ == "__main__":
    main()
