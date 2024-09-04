# # Write a program that finds all the numbers from 1 to 1000 that are divisible by 6.


def programs():
    program = [numbers for numbers in range(1, 1001) if numbers % 6 == 0]
    return program

print(programs())