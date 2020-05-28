import time
import sys #this allows you to use the sys.exit command to quit/logout of the application
import agent
import recognise

def main():
    """Main function which runs the menu() function to display details on console"""
    menu()

def credentials():
    """Runs the agent.py code"""
    agent.main()
def faceRecog():
    """Runs the facial recognition code"""
    recognise.main()

def menu():
    """Prints out a menu which prompts the user to either login with credentials or face scan"""
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

# Execute program.
if __name__ == "__main__":
    main()
