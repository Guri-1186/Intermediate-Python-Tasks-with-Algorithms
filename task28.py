# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
def length_counts(sa_countries):
  counts = {}
  for word in sa_countries:
      length = len(word)
      counts[length] = counts.get(length, 0) + 1
  return counts
print(length_counts(sa_countries))


