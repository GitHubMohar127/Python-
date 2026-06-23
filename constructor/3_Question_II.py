# Question 2

# Create a Car class.

# Constructor:

# brand
# model

# Create 3 objects and print their details.


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        self.display()

    def display(self):
        print(f"Brand : {self.brand}, Model : {self.model}")
    

c1 = Car("BMW", 1234)
c1 = Car("xxx", 4567)
c1 = Car("yyy", 0000)
