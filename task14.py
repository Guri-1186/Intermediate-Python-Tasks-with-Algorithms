# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in 
    
    
def cleanup(lst):
  clean_list = [word for word in lst if word.strip() != ""]
  return " ".join(clean_list)
    
print(cleanup(["cat", "er", "pillar"])         ) #  => "cat er pillar"
print(cleanup(["cat", " ", "er", "", "pillar"])) #  => "cat er pillar"
print(cleanup(["", "", " "])                   ) #  => ""