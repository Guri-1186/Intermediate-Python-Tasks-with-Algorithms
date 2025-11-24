#update key
personal_info = {"name":"loli", "age": 40, "phone_number":12345}
def udpate_dict():
    old_key = input("Enter key wich you want update :")
    new_key = input("Enter a new key :")
    personal_info[new_key] = personal_info.pop(old_key)
    
    return personal_info

print(udpate_dict())