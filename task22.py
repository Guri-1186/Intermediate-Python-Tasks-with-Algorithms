

# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
def greater_sum(lst1,lst2):
    if sum(lst1) > sum(lst2):
        return lst1
    else:
        return lst2
   
      
print( greater_sum([1, 2, 3], [1, 2, 4])) # => [1, 2, 4]
print( greater_sum([4, 5], [2, 3, 6])   ) # => [2, 3, 6]
print( greater_sum([1], [])             ) # => [1]
