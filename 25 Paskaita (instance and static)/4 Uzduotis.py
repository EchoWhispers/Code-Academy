class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.list = []


    def __str__(self):

        return f"Employee name: {self.name}, Salary: {self.salary}"

    @staticmethod
    def calculate_payroll():
        return f"Total employees salary: {sum(employee.salary for employee in employees)}"


e1 = Employee("Alice", 2000)
print(e1)
e2 = Employee("Bob", 1800)
print(e2)
e3 = Employee("Amber", 2500)
print(e3)


employees = [e1, e2 , e3]
print(Employee.calculate_payroll())

e4 = Employee("Tom", 1950)
print(e4)
employees.append(e4)
print(Employee.calculate_payroll())


        # e5 = Employee("Charlie", 5500)
        # employees.append(e5)
