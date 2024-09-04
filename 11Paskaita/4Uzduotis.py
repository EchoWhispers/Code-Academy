# Write a program that prompts the user to enter a text string and then calculates how many words in the text have more than five characters.


def program(text):
    return sum(1 for word in text.split() if len(word) > 5)
user = input("Enter text here: ")

count = program(user)

print(f" There is {count} words that a longer then 5 letters")