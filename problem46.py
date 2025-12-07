#create a dictionary from existing dictionary, wich display length of words as value
person = {
    "name": "Alex",
    "age": 16,
    "city": "Tbilisi"
}

my_dict = {key:len(str(value)) for key, value in person.items()}
print(my_dict)