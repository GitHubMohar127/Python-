# Question 5 (Interview Level)

# Create a VotingSystem class.

# Private variable:

# __age

# Setter validation:

# age >= 18

# Method:

# can_vote()

# Return:

# True

# if age is valid.

class Votingsystem:

    def __init__(self):
        self.__age = 12

    def get_age(self):
        return self.__age

    def can_vote(self):
        if self.__age > 18:
            print("Can Vote")
        else:
            print("Not")

v1 = Votingsystem()

v1.can_vote()

print(v1.get_age())

