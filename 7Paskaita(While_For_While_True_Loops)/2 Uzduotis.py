# Allow the user to enter 10 integers, then print the sum and average of those entered numbers.
#
#
# Enter integer 1: 5
# Enter integer 2: 3
# ...
# Enter integer 10: 2
# Sum: 45, Average: 4.5



numbers = []

while len(numbers) < 10:
    num = int(input("Enter integer: "))
    numbers.append(num)
average = sum(numbers)/len(numbers)
print("Sum:", sum(numbers), "Average:", average)
