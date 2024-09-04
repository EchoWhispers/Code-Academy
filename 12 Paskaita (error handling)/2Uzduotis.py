# In Python, dividing by zero raises a ZeroDivisionError. Your task is to create a function that:

# Tries to divide the first number by the second number.
#
# If the second number is zero, it should catch the ZeroDivisionError and return a custom error message.
#
# If the division is successful, it should return the result.
#
# Regardless of whether the division is successful or not, it should print a message saying ("Attempted division."
#                                                                                            " If the inputs are not numbers, it raises a TypeError. "
#                                                                                            "It catches this TypeError and returns a custom error message.)
def calc():
    try:
        num1 = float(input("Enter firsts number: "))
        num2 = float(input("Enter second number: "))
    except ValueError as e:
        raise TypeError("only numbers")
    symbol = input("Enter simbol: ")

    if symbol == "+":
        result = num1 + num2
        return result
    elif symbol == "-":
        result = num1 - num2
        return result
    elif symbol == "*":
        result = num1 * num2
        return result
    else:
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print()
        finally:
            print("Attempted division")

    return "division from 0 imposible"

while True:
    try:
        print(calc())
    except TypeError as e:
        print("only numbers")
        break


