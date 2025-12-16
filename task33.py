# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#

my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

def common_elements(my_dict):  # => ["A", "D"]
    result = []

    for key in my_dict:
        if key in my_dict.values():
            result.append(key)

    return result

print(common_elements(my_dict))
