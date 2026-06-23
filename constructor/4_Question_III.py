# Create an Employee class.

# Constructor:

# name
# salary

# Add a method:

# display()

# Output:

# Name: Mohar
# Salary: 50000

class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

s1 = Employee("Mohar", 21000)
s1.display()
