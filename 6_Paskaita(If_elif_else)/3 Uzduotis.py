# # Write a small calculator application that allows the user to enter two numbers and a symbol
# # (+, -, *, /) to perform the operation and print the result.
#
#
# Enter the first number: 7
# Enter the symbol: *
# Enter the second number: 6
# The result of 7 * 6 is 42.


first = float(input("Enter the first number: "))
symbol_ = input("Enter the symbol (+, -, *, /): ")
second = float(input("Enter the second number: "))

if symbol_ == "+":
    result = first + second

elif symbol_ == "-":
    result = first - second

elif symbol_ == "*":
    result = first * second

else:
    result = first / second
print(f" The result of {first} {symbol_} {second} is" ,result)




