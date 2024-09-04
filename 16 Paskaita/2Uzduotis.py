# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
#
# Form the fullname by simply joining the first and last name together, separated by a space.
#
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.


class Employee:

    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def __str__(self):

        return (
            f"Your full name is : {self.name} {self.lname}\n"
            f"Your email address is : {self.name}.{self.lname}@company.com".lower())
name = input("Enter your first name: ")
lname = input("Enter your last name:")

a = Employee(name= name, lname= lname)
print(a)