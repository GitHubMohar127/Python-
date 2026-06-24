# Question 4 (Interview Level)

# Create a Validator class.

# Static methods:

# is_even(num)
# is_odd(num)

# Examples:

# Validator.is_even(10)
# # True

# Validator.is_odd(7)
# # True

class Validator:

    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            print("Even")
    
    @staticmethod
    def is_odd(num):
        if num % 2 != 0:
            print("Odd")

Validator.is_even(10)
Validator.is_odd(7)