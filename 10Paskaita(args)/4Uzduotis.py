# # Create a function that checks if every bigram from a given list of bigrams can be found at least once in a provided list of words.
#
#
# bigrams_words = (["at", "be", "th", "au"]), (["wolf", "sun", "thorn", "dog"])
#
# #
#
# def ieskomas(bigrams, words):
#     bigrams_words = list(zip(words, [word[1:] for word in words[1:]]))
#     for bigrams in bigrams_words:
#         if bigrams in bigrams_words:
#             return True
#         else:
#             return False
#
# print(ieskomas("bigrams", "words"))


def can_find(bigrams, words):
    return all(any(bigram in word for word in words) for bigram in bigrams)
print(can_find(["at", "be", "th", "au"], ["lol", "tro", "bet", "dog"]))

# def ieskomas(bigrams, words):
#     return all(any(bigrams in word))
#         for word in words:
#             for bigram in bigrams:
# print(ieskomas(["at", "be", "th", "au"],["lol", "tro", "grey", "dog"]))