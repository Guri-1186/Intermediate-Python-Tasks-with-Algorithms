# Declare a ength_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.

#solution 1
def length_match(lst, num):
    result = []
    for value in lst:
        if len(value) == num:
            result.append(value)
    return len(result)

#solution 2            
def length_match(lst, num):
    count = 0
    for value in lst:
        if len(value) == num:
            count+=1
    return count
                   

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3)) #  => 2
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5)) #  => 1
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4)) #  => 0
print(length_match([], 5))    # ) #