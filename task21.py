# Declare count_of_a function that accepts a list of strings #
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
def count_of_a(lst):
    return list(map(lambda word: word.count("a"),lst))
print(count_of_a(["alligator", "aardvark", "albatross"])) #   => [2, 3, 2]
print(count_of_a(["plywood"])                           ) #   => [0]
print(count_of_a([])                                    ) #   => []