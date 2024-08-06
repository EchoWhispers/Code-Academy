#Allow the user to enter two numbers. Print out which one is higher, or if they are equal.

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two:"))

if number_one > number_two:
    print(f"Number {number_one} is higher")
elif number_one < number_two:
    print(f"Number {number_two} is higher")
else:
    print(f"{number_one} and {number_two} it is equal!")
