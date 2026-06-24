# Question 3

# Create an Employee class.

# Private variable:

# __salary

# Add validation:

# salary > 0

class Employee:

    def __init__(self):
        self.__salary = 0
    
    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if self.__salary <= 0:
            print("Adding Amount")
            self.__salary += amount
        else:
            print(f"{self.__salary} present in the account")

e1 = Employee()

print(e1.get_salary())

e1.set_salary(2000)

print(e1.get_salary())

e1.set_salary(2000)