#!/usr/bin/env python3
# Documentation: https://docs.python.org/3/library/socket.html
import socket, json, sqlite3, sys
sys.path.append("..")
import socket_utils
from datetime import datetime

HOST = "220.244.177.218"         # The server's hostname or IP address.
PORT = 63000               # The port used by the server.
ADDRESS = (HOST, PORT)
carid = 1

def main():
    """Main Function prompting the user to enter their Username and Password"""
    username = input("Enter username:")
    password = input("Enter password:")
    user = { "username": username, "password": password, "carid": carid, "finish": 0, "date": str(datetime.now())}
    login(user)

def login(user):
    """
 - Prompts the user to Login and connects with Master Pi
 - Gives the user 2 options with their car
 - Either to Unlock or Return"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Connecting to {}...".format(ADDRESS))
        s.connect(ADDRESS)
        print("Connected.")

        print("Logging in as {}".format(user["username"]))

        print("Waiting for Master Pi...")
        while(True):
            print()
            choice = input("""
Please choose to either:
 1: Unlock Car
 2: Return Car

 Please enter your choice: """)
            if choice == "1":  
                user["finish"] = 0
                break             
            elif choice == "2":
                
                user["finish"] = 1
                break
                
            else:
                print("\n You must only select either 1 or 2")
                print(" Please try again\n")
                print()

        socket_utils.sendJson(s, user)
        while(True):
            
            object = socket_utils.recvJson(s)
            if("authenticated" in object):
                print("Car Unlocked")
                print()
                break
                
            elif("returned" in object):
                print("Car Returned")
                print()
                break
            elif("nope" in object):
                print("Not Authorized")
                print()
                break
            elif("nobooking" in object):
                print("No Booking Found")
                print()
                break

# Execute program.
if __name__ == "__main__":
    main()
