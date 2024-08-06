# # Write a Python program that defines two variables containing strings for a username and password.
# # Start an endless loop allowing the user to enter a username and password.
# # If the credentials are correct, stop the endless loop and print a greeting message.
#
#
# Enter username: admin
# Enter password: 1234
# Enter username: user123
# Enter password: securepass

while True :

    username = input("Enter username: ").lower()
    if username == "admin":
        password = input("Enter password: ").lower()
        if password == "1234":
            print("Welcome on board")
            break
        else:
            print("Incorect password")
    else:
        print("Incorect username")