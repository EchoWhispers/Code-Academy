# Write a function that takes two lists of integers and returns
# True if each corresponding pair of elements from the two lists adds up to the same value across all pairs.
# Otherwise, return False.

# puzzle_pieces = ([1, 2, 3, 4], [4, 3, 2, 1])
#puzzle_pieces = ([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6])
#puzzle_pieces = ([1, 2], [-1, -1])
#puzzle_pieces =([9, 8, 7], [7, 8, 9, 10])

#puzzle_pieces = ([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6])


def puzzle_pieces(a, b):
    if len(a) == len(b):
        return True
    suma = a[0] + b[0]
    return all(a[i] + b[i] == suma for i in range(len(a)))
print(puzzle_pieces([1, 2], [-1, -1]))


