# Write a program that prompts the user to input a string and calculates the occurrence of each letter in the string, storing the results in a dictionary.
#
#
# from collections import Counter
#
# def calculate_letter_occurrences(text):
#     # Filter out non-alphabetic characters and convert to lower case for uniformity
#     filtered_text = filter(str.isalpha, text.lower())
#     return dict(Counter(filtered_text))
#
# user_text = input("Please enter your text: ")
# letter_counts = calculate_letter_occurrences(user_text)
#
# print("Letter occurrences:", letter_counts)