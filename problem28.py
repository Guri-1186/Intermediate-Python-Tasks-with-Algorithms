#find a maximum key in dictionary
students = {
    10: "Gio",
    27: "Lika",
    3: "Nika",
    49: "Ana"
}
#version 1
def max_keys(students):
    result = []
    for key in students.keys():
        result.append(key)
    return max(result)


#version 2
def max_keys (students):
    return max(students.keys())
print(max_keys(students))