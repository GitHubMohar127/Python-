# Question 1: Person → Student

# Create:

# Person
#    ↓
# Student

# Requirements:

# Person:
#     name

#     show_name()

# Student:
#     marks

#     show_marks()

# Expected Output:

# Name: Mohar
# Marks: 90

class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_marks(self):
        print(self.marks)

c1 = Student("Mohar", 32)
c1.show_name()
c1.show_marks()