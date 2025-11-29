# write a program to get total length of all keys of a dictionary with string keys

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def length_of_keys():
    keys = 0
    for key in thisdict.keys():
        keys+= len(key)

    return keys
        

print(length_of_keys())
        
    