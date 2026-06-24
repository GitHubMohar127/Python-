# Question 1

# Create a Calculator class.

# Add static methods:

# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)

class Calculator:
    
    @staticmethod
    def add(num1, num2):
        print(num1 + num2)
    
    @staticmethod
    def subtract(num1, num2):
        print(num1 - num2)
    
    @staticmethod
    def multiply(num1, num2):
        print(num1 * num2)
    
    @staticmethod
    def divide(num1, num2):
        print(num1 // num2)


c1 = Calculator()

c1.add(6,3)
c1.subtract(6,3)
c1.multiply(6,3)
c1.divide(6,3)
