# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}

def invert(my_dict):  # => {'B': 'A', 'D': 'C', 'F': 'E'}
    new_dict = {value: key for key, value in my_dict.items()}
    return new_dict

print(invert(my_dict))
