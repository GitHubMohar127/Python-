# class Student:
    
#     def __init__(self):
#         print("Object Created")
    
# s1 = Student()

class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

s1 = Student("Mohar", 21)
s1.display()
