# # # Write a Python program that uses a for loop to generate and print the first 10 numbers of the Fibonacci sequence.
# # # In the Fibonacci sequence, each number is the sum of the two preceding ones, starting from 0 and 1.
# # #
# # #
# # # Fibonacci sequence: 0 1 1 2 3 5 8 13 21 34
# #
# #
# fib1 = 0
# fib2 = 1
#
# print(fib1)
# print(fib2)
#
# for i in range(8):
#     fib_next = fib1 + fib2
#     print(fib_next)
#     fib1 = fib2
#     fib2 = fib_next

fib1 = 0
fib2 = 1

for x in range(8):
    suma_fib1_ir_fib2 = fib1 + fib2
    fib1 = fib2
    fib2 = suma_fib1_ir_fib2
    print(f"Fibonacci sequence: {suma_fib1_ir_fib2}")




