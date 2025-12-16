# Declare a count_of_value function at accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
my_dict = { "a" : 5, "b" : 3, "c" : 5 }

def count_of_value(my_dict, number):
    count = 0
    for key, value in my_dict.items():
        if value == number:
            count+=1
    return count
    
    
print(count_of_value(my_dict, 5))  # => 2
print(count_of_value(my_dict, 3))  # => 1