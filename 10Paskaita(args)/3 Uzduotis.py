# Write a function that determines the difference in sums between even and odd numbers from a given list of integers.


war_of_numbers = [2, 8, 7, 5, 4, 8, 55]

def even_odd():
    even_sum = sum(x for x in war_of_numbers if x % 2 == 0)
    odd_sum = sum(x for x in war_of_numbers if x % 2 != 0)
    x = abs(even_sum - odd_sum)
    return x

print(even_odd())

