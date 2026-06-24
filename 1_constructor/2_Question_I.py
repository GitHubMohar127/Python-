# Question 1

# Create a Book class.

# Constructor should accept:

# title
# author
# price

# Print all details

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

        self.Dispaly()
    
    def Dispaly(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price : {self.price}")

b1 = Book("kakababu", "Sunil Gnguly", 1200)
