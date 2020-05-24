import time
import sys #this allows you to use the sys.exit command to quit/logout of the application
import agent

def credentials():
    agent.main()
def faceRecog():
    import recognise

def menu():
    print(" Welcome!")
    time.sleep(1)

    choice = input("""
Please choose to either:
 1: Enter your account details
 2: Facial Recognition

 Please enter your choice: """)

    if choice == "1":
        credentials()
    elif choice == "2":
        faceRecog()
    else:
        print("\n You must only select either 1 or 2")
        print(" Please try again\n")
        menu()

menu()