# Create a function that validates an email address based on user input.
# Ensure the email address contains exactly one "@" symbol and at least one "." in the domain part, along with other structural validations.
#
#
# Enter an email address: example@gmail.com
# The email address is valid. example@gmail.com
# The email address is valid.
from string import ascii_letters, digits
def email_printed():

    email = input("Enter an email address: ")

    if email.count('@') == 1:
        local , domain = email.split("@")
        if not local or not domain:
            print("The email address is invalid.")
        elif local.startswith("@") or local.endswith("@"):
            print("The email address is invalid.")
        elif not "." in domain:
            print("The email address is invalid.")
        elif domain.startswith(".") or domain.endswith("."):
            print("The email address is invalid.")
        elif ".." in email:
            print("The email address is invalid.")
        else:
            print("The email address is valid.")
    else:
        print("The email address is invalid.")

email_printed()
