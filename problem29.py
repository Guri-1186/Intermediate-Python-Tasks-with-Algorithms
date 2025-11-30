#write a program to update any value in a dictionary on user request

students = {
    10: "Gio",
    27: "Lika",
    3: "Nika",
    49: "Ana"
}

def update_dict(students):
    key = int(input("Enter key which value you want to update: "))
    new_value = input("Enter new value: ")
    
    if key in students:
        students[key] =  new_value
        return students
    else:
        return "Key not found"

 

print(update_dict(students))
