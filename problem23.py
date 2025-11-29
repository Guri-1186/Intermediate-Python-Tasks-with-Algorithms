# write a python program to print a dictionary line by line ke and valu should have one tab distance
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key,value in thisdict.items():
    print(f"{key} \t{value}")