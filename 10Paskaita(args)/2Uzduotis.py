# # Write a lambda function that takes a string and a number, and returns the string repeated that number of times.
# from typing import Tuple, Callable, Any
#
#
# #def stringas():
#     (lambda x, y: x * y, (5, 3))
#     return stringas
# print(x)

def stringas():
    x = (lambda x, y: x * y)("Hello world ,", 3)
    return x

print(stringas())