# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
def  encrypt_message(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for el in char:
        index_postion = (alphabet.index(el) + 2) % 26
        result+=alphabet[index_postion]
      
    
    return result
        
print(encrypt_message("abc")) # => "cde"
print(encrypt_message("xyz")) # => "zab"
print(encrypt_message("")   ) # => ""