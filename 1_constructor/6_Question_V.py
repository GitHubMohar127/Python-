# Create a Student class.

# Constructor:

# name
# marks

# Add a method:

# is_pass()

# Return:

# True

# if marks ≥ 40 else

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
        self.is_pass()
    
    def is_pass(self):
        if self.marks >= 40:
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")

s1 = Student("Mohar", 60)
s2 = Student("XXX", 20)