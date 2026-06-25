# Question 2: Vehicle → Car

# Create:

# Vehicle
#    ↓
# Car

# Methods:

# Vehicle:
#     start()

# Car:
#     drive()

# Output:

# Vehicle Started
# Car is Driving

class Vehicle:

    def start(self):
        print("Viehicle Statrted")

class Car(Vehicle):

    def drive(self):
        print("Car is Driving")

c1 = Car()
c1.start()
c1.drive()