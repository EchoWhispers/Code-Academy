# class MathOp:
#     @classmethod
#     def factorial(cls, number):
#         if number == 0:
#             return 1
#         else:
#             return number * cls.factorial(number-1)
#
# print(MathOp.factorial(4))

number = int(input("Enter factorial Number:"))
factorial = 1
while number > 0:
    factorial *= number
    number -=1
print(factorial)













# User input: You prompt the user to input a number and convert it to an integer using int().
# Initialize factorial = 1: This ensures you have a starting value for multiplication that won't affect the result negatively.
# While loop condition: The loop runs as long as the number is greater than zero.
# Multiplication: Inside the loop, you multiply the factorial variable by the current value of the user-provided number. This keeps updating factorial with the running product.
# Decrement the number: After multiplying, you decrease the number by 1 (number -= 1).
# Repeat: The loop continues until the number becomes zero, at which point it stops.
# Print the result: Finally, you print the factorial variable which now holds the computed factorial of the input number.
# When you perform factorial = factorial * number inside the loop, the factorial variable is updated in every iteration with the new result. Here's how it works:

# First iteration:
#
# If the number is, say, 5, and factorial is initialized to 1:
# factorial = 1 * 5 = 5 → now factorial holds 5.
# Second iteration:
#
# The number is decremented to 4.
# factorial = 5 * 4 = 20 → now factorial holds 20.
# Third iteration:
#
# The number is decremented to 3.
# factorial = 20 * 3 = 60 → now factorial holds 60.
# Fourth iteration:
#
# The number is decremented to 2.
# factorial = 60 * 2 = 120 → now factorial holds 120.
# Fifth iteration:
#
# The number is decremented to 1.
# factorial = 120 * 1 = 120 → factorial still holds 120.