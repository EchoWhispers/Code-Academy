def calc():
    try:
        num1 = float(input("Enter firsts number: "))
        num2 = float(input("Enter second number: "))
    except ValueError as e:
        raise TypeError("please enter only numbers. Error: ", e)

    symbol = input("Enter simbol: ")

    if symbol == "+":
        result = num1 + num2
    elif symbol == "-":
        result = num1 - num2
    elif symbol == "*":
        result = num1 * num2
    else:
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return "division from 0 imposible"
        finally:
            print("Attempted division")
    return result


while True:
    try:
        print(calc())
    except TypeError as e:
        print("Error: ", e)
    else:
        break
