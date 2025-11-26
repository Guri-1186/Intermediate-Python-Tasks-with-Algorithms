class Student:
    def __init__ (self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    def __str__ (self):
        return f"{self.name}, {self.student_id}"
    
    
student = Student("loli", 345)
print(student)