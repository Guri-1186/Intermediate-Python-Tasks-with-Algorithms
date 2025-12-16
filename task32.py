# Declare a sum_of_value function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
my_dict = { "a": 5, "b": 3, "c": 10 }
def sum_of_values(my_dict, lst):
    result = 0
    for key, value in my_dict.items():
        if key in lst:
            result+=value
    return result

  
    
print(sum_of_values(my_dict, ["a"]) )   #        => 5
print(sum_of_values(my_dict, ["a", "c"]))   # => 15
print(sum_of_values(my_dict, ["a", "c", "b"])) # => 18
print(sum_of_values(my_dict, ["z"]))         #  => 0