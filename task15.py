# Define a ested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
def nested_sum(lst_of_lsts):
    total = 0
    for sublist in lst_of_lsts:
        for num in sublist:
            total += num
    return total
    
print(nested_sum([[1, 2, 3], [4, 5]])          ) #  => 15
print(nested_sum([[1, 2, 3], [], [], [4], [5]])) #  => 15
print(nested_sum([[]])                         ) #  => 0

