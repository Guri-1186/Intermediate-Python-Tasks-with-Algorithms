#write a program to sort dictionary by key
personal_info = {"name":"loli", "age": 40, "phone_number":12345}
def sort_items(personal_info):
   view = sorted(personal_info.items())
   return view

print(sort_items(personal_info))

# sorted by value
personal_info = {"name": "loli", "age": 40, "phone_number": 12345}

def sort_by_value(personal_info):
    return sorted(personal_info.items(), key=lambda item: str(item[1]))

print(sort_by_value(personal_info))
