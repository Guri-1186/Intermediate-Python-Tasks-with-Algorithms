#write a program to store students record,user will be able to delete zny student from a record on run time
names = []
def record():
    for i in range(5):
        name = input(f"Enter student {i+1} name: ")
        if name.isalpha():
            names.append(name)
    return names
print(record())

def clear_list():
    students_name = input("Enter students name you would like to delete: ")
    if students_name in names:
     names.remove(students_name)
     return names
    else:
        return "Name not found in the record"
 


print(clear_list())
