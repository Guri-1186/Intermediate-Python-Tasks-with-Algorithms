# write a program to store keys and values into seperate list
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
def seperate_key_value(thisdict):
    keys = []
    values = []
    for key, value in thisdict.items():
        keys.append(key)
        values.append(value)
        
    return f"Keys: {keys}  - Values {values}"
print(seperate_key_value(thisdict))