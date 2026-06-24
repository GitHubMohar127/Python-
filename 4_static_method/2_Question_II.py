# Question 2

# Create a Temperature class.

# Static method:

# celsius_to_fahrenheit(c)

# Formula:

# (c * 9/5) + 32

class Temprature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

print(Temprature.celsius_to_fahrenheit(100))