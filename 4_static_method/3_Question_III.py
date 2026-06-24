# Question 3

# Create a Student class.

# Static method:

# is_pass(mark)

# Return:

# True

# if mark ≥ 40 else

# False

class Student:
    def is_pass(mark):
        if mark >= 40:
            return True
        else:
            return False

print(Student.is_pass(10))