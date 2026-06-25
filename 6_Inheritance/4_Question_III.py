# Question 3: Animal → Dog

# Create:

# Animal
#    ↓
# Dog

# Methods:

# Animal:
#     eat()

# Dog:
#     bark()

# Output:

# Eating
# Woof Woof

class Animal:
    @staticmethod
    def eat():
        print("Eating")

class Dog(Animal):
    @staticmethod
    def bark():
        print("Woof Woof")

d1 = Dog()
d1.bark()
d1.eat()
