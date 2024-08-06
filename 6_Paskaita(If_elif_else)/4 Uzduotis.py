# # Write a Python program that asks the user for their membership status, age, and if necessary,
# # whether an adult accompanies them to determine their eligibility to loan different types of books from a library:
# # Only members can loan books.
# # Members aged 12 or older or those under 12 accompanied by an adult can loan all books
# # Members under 12 not accompanied by an adult can only loan children’s books.
# # The program should use and, or, and not logical operators to check conditions and output appropriate messages based on user input.
#
#
# Are you a library member? (yes/no): yes
# Enter your age: 14
# You can loan all books.
#
# Are you a library member? (yes/no): yes
# Enter your age: 10
# Is an adult accompanying you? (yes/no): no
# You can only loan children's books.
#
# Are you a library member? (yes/no): no
# You cannot loan any books.


member = input("Are you a library member? (yes/no): ").lower()

if member == "yes":
    age = int(input("Enter your age: "))

    if age >= 12:
        print("You can loan all books.")
    elif age < 12:
        adult = input("Is an adult accompanying you? (yes/no): ").lower()
        if adult == "yes":
            print("You can loan all books.")
        else:
            print("You can only loan children's books.")
else:
    print("You cannot loan any books.")