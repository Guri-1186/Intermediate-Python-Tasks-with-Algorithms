# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES

def fancy_concatenate( lists):
    final = ""
    for row in lists:
        if len(row) == 3:
            for string in row:
                final+=string
    return final
            
        
print(fancy_concatenate([["A", "B", "C"]])                      ) #  => "ABC"
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])     ) #  => "ABCDEF"
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])) #  => "ABC"
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]])          ) #  => "ABC"
print(fancy_concatenate([["A", "B"], ["C", "D"]])               ) #  => ""