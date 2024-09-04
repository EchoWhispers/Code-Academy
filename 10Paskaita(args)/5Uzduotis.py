# Create a function that filters a list of strings and returns a new list containing only those that start with a vowel.


def start_with_vowel(strings):
    return list(filter(lambda word: word[0] in 'aoiue', strings))

print(start_with_vowel(["apple", "banana", "orange"]))