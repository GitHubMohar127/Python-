# How to use Getter and setter Methords 

class Bankaccount:

    def __init__(self):
        self.__balance = 1000
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance += amount 

account = Bankaccount()

print(account.get_balance())
account.set_balance(500)
print(account.get_balance())