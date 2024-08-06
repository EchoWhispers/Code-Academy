#dictionary = {
#     "apple": "a fruit that grows on trees",
#     "book": "a set of printed pages, bound together, containing text or pictures",
#     "computer": "an electronic device for storing and processing data"
# }


my_dict = {
    "apple": "a fruit that grows on trees",
    "book": "a set of printed pages, bound together, containing text or pictures",
    "computer": "an electronic device for storing and processing data"

}
x = input("Enter a word Apple, Book or Computer to look up its meaning:").lower()

if x in my_dict:
    print(f"Meaning of the word",  x , "is:", my_dict[x])
else:
    print("This word is not in our dictionary.")