# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. Initiate class and show up some calculations.


class Calculator:

    def __init__(self, number1 , number2, opr):
        self.number1 = number1
        self.number2 = number2
        self.opr = opr

    def calculate(self):
        if self.opr == "+":
            return  self.number1 + self.number2

        elif  self.opr == "-":
            return  self.number1 - self.number2

        elif self.opr == "*":
            return  self.number1 * self.number2

        elif self.opr == "/":
            try:
                return  self.number1 / self.number2
            except ZeroDivisionError:
                print("No division from 0 possible!")
        else:
            return print("Invalid opperation")

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
opr = input("Enter + - * / ")


calc = Calculator(number1, number2, opr)

result = calc.calculate()
print(result)



