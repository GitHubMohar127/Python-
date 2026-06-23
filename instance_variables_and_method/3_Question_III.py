class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdrawl(self, amount):
        self.balance = self.balance - amount
    
    def view_balance(self):
        print(self.balance)

a1 = Account("Mohar", 1000)
a1.deposit(500)
a1.withdrawl(1000)
a1.view_balance()