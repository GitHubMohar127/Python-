# Question 1

# Create a Car class.

# Class Variable:

# wheels = 4

# Instance Variables:

# brand
# price

# Create 3 objects and print all details.

class Car:
    wheels = 4

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def dispaly(self):
        print(self.brand, self.price)
        print(Car.wheels)

s1 = Car("BMW", 200000)
s2 = Car("XXX", 300000)
s3 = Car("VVVV", 40000)

s1.dispaly()
s2.dispaly()
s3.dispaly()