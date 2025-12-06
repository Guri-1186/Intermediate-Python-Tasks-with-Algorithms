# Define aPrint(in_list function that accepts ) #a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.

def in_list(lst, word):
    for index, value in enumerate(lst):
        if value == word:
            return index
    return -1 

strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "enchanted") ) # ==> 0
print(in_list(strings, "sparks fly")) # ==> 1
print(in_list(strings, "fifteen")   ) # ==> -1
print(in_list(strings, "love story")) # ==> -1

