# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
def only_odds(lst):
    return list(filter(lambda num : num%2 == 1 ,lst))
    
print(only_odds([1, 3, 5, 6, 7, 8])) #     =>  [1, 3, 5, 7]
print(only_odds([2, 4, 6, 8]))      #    =>  []