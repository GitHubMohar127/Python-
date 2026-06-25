# Question 5: Multilevel Inheritance

# Create:

# Animal
#    ↓
# Dog
#    ↓
# Puppy

# Methods:

# Animal:
#     eat()

# Dog:
#     bark()

# Puppy:
#     play()

# Output:

# Eating
# Woof
# Playing

class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Woof")
class Puppy(Dog):
    def play(self):
        print("Playing")

p1 = Puppy()

p1.eat()
p1.bark()
p1.play()