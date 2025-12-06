# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
def long_strings(lst):
    result = []
    for char in lst:
        if len(char) >= 5:
            result.append(char)
    return result
            
    
print(long_strings(["Hello", "Goodbye", "Sam"])) #  => ["Hello", "Goodbye"]
print(long_strings(["Ace", "Cat", "Job"])      ) #  => []
print(long_strings([])                         ) #  => []
