# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
def to_dictionary(detectives): # => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}
    d_detectives = {}
    for index, word in enumerate(detectives):
        d_detectives[word] = index
    return d_detectives
    
    
print(to_dictionary(detectives))