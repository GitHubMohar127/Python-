# Question 7: Bank Account

# Create:

# Account
#    ↓
# SavingsAccount

# Account:

# balance
# deposit()

# SavingsAccount:

# withdraw()

class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Total Amount: ", self.balance)

class SavingsAccount(Account):
    def __inti__(self, balance):
        super().__init__(balance)
    
    def withdral(self, amount):
        self.balance -= amount
        print("Withdral Amount", amount)
        print("Total Amount : ", self.balance)

s1 = SavingsAccount(1000)
s1.deposit(500)
s1.withdral(200)
