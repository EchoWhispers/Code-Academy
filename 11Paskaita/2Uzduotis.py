# # # Find all numbers from 1 to 1000 that have the digit 9 in them.
# #
# #
def program():
    finding = [number for number in range(1, 1001) if "9" in str(number)]
    return finding
print(program())
