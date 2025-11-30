# write a program to create dictionary wich display those value wich have vowel character

thisdict = {
  "brand": "Ford",
  "model": "Mustang"
}

def vowel_value(thisdict):
    vowels = "aeiou"
    for value in thisdict.values():
        for char in value.lower():
            if char in vowels:
               break
            print(value)
            
             
vowel_value(thisdict)