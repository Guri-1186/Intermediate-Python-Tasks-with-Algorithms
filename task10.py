# Declare delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES

def delete_all(lst, num):
    while num in lst:
        lst.remove(num)
    return lst
         
print(delete_all([1, 3, 5], 3)) #  => [1, 5]
print(delete_all([5, 3, 5], 5)) #  => [3]
print(delete_all([4, 4, 4], 4)) #  => []
print(delete_all([4, 4, 4], 6)) #  => [4, 4, 4]

