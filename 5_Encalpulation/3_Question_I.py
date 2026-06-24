# Question 1

# Create a Student class.

# Private variable:

# __marks

# Methods:

# get_marks()
# set_marks()

# Only allow marks between 0 and 100.

class Student:

    def __init__(self):
        self.__mark = 0
    
    def get_marks(self):
        return self.__mark
    
    def set_marks(self, mark):
        if 0 <= mark <= 100:
            self.__mark = mark

s = Student()

print(s.get_marks())

s.set_marks(89)

print(s.get_marks())

