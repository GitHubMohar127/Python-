# Create a Mobile class.

# Constructor:

# brand
# price

# Create two mobiles and compare their prices.


class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def compare_price(self, other_mobile):
        if self.price > other_mobile.price:
            print(f"{self.brand} is more expensive then {other_mobile.brand}")
        else:
            print(f"{other_mobile.brand} is more expensive then {self.brand}")

mobile1 = Mobile("Sumsung", 20001000)
mobile2 = Mobile('Iphone', 100000)

mobile1.compare_price(mobile2)