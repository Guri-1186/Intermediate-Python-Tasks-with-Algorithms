# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES

def same_index_values(lst1,lst2):
    result = []
    for index, value in enumerate(lst1):
        if value == lst2[index]:
            result.append(index)
    return result
        
print(same_index_values([1, 2, 3], [3, 2, 1]))                        # => [1]
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # => [1, 3]