# Access specifier
#     1. Public
#     2. Private
#     3. Protected

# How to work with Public Access Speccifiers
class Student:

    def __init__(self):
        self.name = "Mohar"
    
s = Student()

print(s.name)

# How to work with Protected Access Specifiers
class Student:
    def __init__(self):
        self._name = "Mohar_1"
s1 = Student()

print(s1._name)

#How to work with Private Access Specifiers
class Student:
    def __init__(self):
        self.__name = "Mohar_2"

s2 = Student()

# print(s2.__name)
# This code not works because the varibale is comes under private 
# For accessing, wh have to use getter and setter mothed

class Student:

    def __init__(self):
        self.__name = "Mohar_3"
    def get_name(self):
        return self.__name

s3 = Student()

print(s3.get_name())