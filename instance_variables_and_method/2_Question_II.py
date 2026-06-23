class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def grade(self):
        if self.marks >= 90:
            print("A")
        elif self.marks >= 75:
            print("B")
        else:
            print("C")


s1 = Student("Mohar", 95)
s2 = Student("Ram", 82)
s3 = Student("XXX", 25)

s1.grade()
s2.grade()
s3.grade()