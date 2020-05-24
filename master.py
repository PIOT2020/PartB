#!/usr/bin/env python3
# Documentation: https://docs.python.org/3/library/socket.html
import socket, json, sys
sys.path.append("..")
import socket_utils
import requests

HOST = ""    # Empty string means to listen on all IP's on the machine, also works with IPv6.
             # Note "0.0.0.0" also works but only with IPv4.
PORT = 63000 # Port to listen on (non-privileged ports are > 1023).
ADDRESS = (HOST, PORT)

def main():
    """
 - Authenticates connection with the Agent Pi
 - Receives credentials such as Username and Password from AgentPi and authenticates it
 - Returns authenticated credentials allowing AgentPi access to log in"""
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

                param = {
                        'username' : user["username"], 
                        'password' : user["password"],
                        'carid' : user["carid"]
                }
                print(user["date"])

                if (user["finish"] == 0):
                    if (user["password"] == "none"):
                        response = requests.get(("http://220.244.177.218:5000/api/findBooking2"), params = param)
                        print(response.text)

                    else:
                        response = requests.get(("http://220.244.177.218:5000/api/findBooking"), params = param)
                        print(response.text)

                    if (response.text == "True"):
                        socket_utils.sendJson(conn, { "authenticated": True })
                    else:
                        socket_utils.sendJson(conn, { "nope": True })

                else:
                    response = requests.get(("http://220.244.177.218:5000/api/returnCar"), params = param)
                    if (response.text == "True"):
                        socket_utils.sendJson(conn, { "returned": True })
                    else:
                        socket_utils.sendJson(conn, { "nobooking": True })

                   



# Execute program.
if __name__ == "__main__":
    main()
