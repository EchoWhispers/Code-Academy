# # Implement a simple dictionary that stores words and their meanings. Allow the user to enter a word and retrieve its meaning.
# # Task Instructions:
# # Pre-populate the dictionary with a few words and their meanings.
# # Prompt the user to enter a word.
# # Display the meaning of the word or an error if the word isn't in the dictionary.
#
#
# dictionary = {
#     "apple": "a fruit that grows on trees",
#     "book": "a set of printed pages, bound together, containing text or pictures",
#     "computer": "an electronic device for storing and processing data"
# }


my_dict = {"apple" , "book" , "computer"}

x = input("Enter a word to look up its meaning:").lower()

if x == "apple":
    print("apple: a fruit that grows on trees")
elif x == "book":
    print("book: a set of printed pages, bound together, containing text or pictures")
elif x == "computer":
    print("computer: an electronic device for storing and processing data")
else:
    print("This word is not in our dictionary")



#
# dictionary = {
#     "apple": "a fruit that grows on trees",
#     "book": "a set of printed pages, bound together, containing text or pictures",
#     "computer": "an electronic device for storing and processing data"
# }
# word = input("Enter a word to look up its meaning: ").lower()
# if word in dictionary:
#     print(f"The meaning of {word} is: {dictionary[word]}")
# else:
#     print("This word is not in our dictionary.")
