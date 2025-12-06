# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.

def sum_of_values_and_indices(lst):
    result = []
    for index, value in enumerate(lst):
        result.append(index + value)
    return sum(result)
       
       
print(sum_of_values_and_indices([1, 2, 3])   ) # => (1 + 0) + (2 + 1) + (3 + 2) => 9
print(sum_of_values_and_indices([0, 0, 0, 0])) # => 6
print(sum_of_values_and_indices([])          ) # => 0