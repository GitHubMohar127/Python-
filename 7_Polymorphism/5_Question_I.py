# Question 1

# Create:

# Animal
#     ↓
# Dog
# Cat
# Cow

# Each class overrides:

# sound()

# Create a loop:

# animals = [Dog(), Cat(), Cow()]

# Call:

# sound()

# for each object

class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Humba")

animal = [Dog(), Cat(), Cow()]

for i in animal:
    i.sound()
