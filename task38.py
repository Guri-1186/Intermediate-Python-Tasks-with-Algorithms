
# Define a remove_duplicates function that accepts a single list as an argument. 
# The function should return a list with all of the duplicates from the original list removed. 
# The order of elements in the returned list is irrelevant.
#
# EXAMPLES:
def remove_duplicates(lst):
    return list(set(lst))
    
    
print(remove_duplicates([1, 2, 1, 2])) #  => [1, 2] or [2, 1]
print(remove_duplicates([1, 2, 3, 4])) # => [1, 2, 3, 4] in some order