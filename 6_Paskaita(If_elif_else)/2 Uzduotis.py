#Write a Python program that asks the user to enter their name, surname, and age.
#The program should print whether the user is allowed to enter an online casino. The age limit is 21.


# Enter your name: John
# Enter your surname: Doe
# Enter your age: 22
# John Doe, you are allowed to enter the casino.


name = input("Enter your name:")
surname = input("Enter your surname:")
age = int(input("Enter your age:"))

if age >= 21 :
    print(f"{name} {surname}, you are allowed to enter the casino.")
else:
    print(f"{name} {surname}, you are NOT allowed to enter the casino. Age limit is 21.")