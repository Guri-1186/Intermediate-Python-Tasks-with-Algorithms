# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
def word_lengths(sentence):
    result = []
    splited_word = sentence.split()
    for word in splited_word:
        result.append(len(word))
    return result
   
    
print(word_lengths("Mary Poppins was a nanny")) #  => [4, 7, 3, 1, 5]
print(word_lengths("Somebody stole my donut") ) #  => [8, 5, 2, 5]