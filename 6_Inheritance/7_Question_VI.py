# Question 6: School System

# Create:

# Person
#    ↓
# Teacher

# Person:

# name
# age

# Teacher:

# subject

# Method:

# display()

# Output:

# Name: Rahul
# Age: 35
# Subject: Mathematics

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def dispaly(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Subject", self.subject)

t1 = Teacher("Mohar", 21, "Math")
t1.dispaly()