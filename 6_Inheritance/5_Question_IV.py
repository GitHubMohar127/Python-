# Question 4: Employee → Developer

# Create:

# Employee
#    ↓
# Developer

# Attributes:

# Employee:
#     name

# Developer:
#     language

# Method:

# display()

# Output:

# Name: Mohar
# Language: Python

class Employee:
    def __init__(self, name):
        self.name = name 

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Language : {self.language}")

d1 = Developer("Mohar", "CPP")
d1.display()
