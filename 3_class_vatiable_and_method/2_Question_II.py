# Question 2

# Create a Student class.

# Class Variable:

# school = "DAV School"

# Create a class method:

# change_school()

# Change school name.

class Student:
    school = "DVA School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print(Student.school)

Student.change_school("XXX School")

print(Student.school)