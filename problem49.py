# create list from existing list that conatin uppercase words

words = ["APPLE", "banana", "grape", "orange"]
new_list = [word for word in words if word.isupper()]
print(new_list)