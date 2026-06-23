class Student:
    def __init__(self, name, age):
        self.name = name     #  --
                             #     | -> Instance Variable 
        self.age = age       #  --

    def dispaly(self):
        print(self.name, self.age)

s1 = Student("Mohar", 21)
s1.dispaly()