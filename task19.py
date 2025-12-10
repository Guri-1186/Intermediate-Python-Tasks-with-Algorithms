# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
def right_words(words, num):
    return list(filter(lambda word: len(word) == num, words))

    
   
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3) ) #    => ['cat', 'dog', 'ace']
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5) ) #    => ['heart']
print(right_words([], 4)                                     ) #    => []