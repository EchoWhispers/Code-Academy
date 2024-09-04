# Create a program to request a specific string to calculate how many words contain the letter 'e'.


def program(text):
    return sum(1 for word in text.split() if 'e' in word)

user_text = input("Please enter your text: ")

words_with_e = program(user_text)

print("Number of words containing 'e':", words_with_e)


