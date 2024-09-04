# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
#
# Form the fullname by simply joining the first and last name together, separated by a space.
#
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.


class Employee:

    def __init__(self, name, lname, fullname, email):
        self.name = name
        self.lname = lname
        self.fullname = fullname
        self.email = email


name = input("Enter your first name: ")
lname = input("Enter your last name:")
fullname = f"Full name: {name.capitalize()} {lname.capitalize()}"
email = (f"Your email address is : {name}.{lname}@company.com").lower()

a = Employee(name= name, lname= lname, fullname= fullname, email= email)

print(a.fullname)
print(a.email)