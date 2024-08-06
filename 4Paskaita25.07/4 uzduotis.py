# Write a Python program to find all prime numbers within a user-specified range. Display the list of prime numbers to the user.


a = int(input("Enter the start of the range:"))
b = int(input("Enter the end of the range:"))
prime = []

for x in range(a, b + 1):
    if x > 1:
        is_prime = True
        for y in range(2, int(x ** 0.5) + 1):
            if (x % y) == 0:
                is_prime = False
                break
        else:
            prime.append(x)

print("Prime numbers:" , prime)




# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# primes = []
# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#
# print("Prime numbers:", primes)

