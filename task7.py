# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES

def only_evens(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result
    
print(only_evens([4, 8, 15, 16, 23, 42])) # => [4, 8, 16, 42]
print(only_evens([1, 3, 5])             ) # => []
print(only_evens([])                    ) # => []
