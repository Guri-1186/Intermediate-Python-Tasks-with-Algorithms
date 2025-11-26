class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, {self.age}"
   
name = input("Enter student name :")   
student_id = input ("Enter student id :")           
person = Person(name, student_id)
print(person)