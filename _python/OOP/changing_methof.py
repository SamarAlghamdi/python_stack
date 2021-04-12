class User:
    def __init__(self,name):
        self.name =name
        self.balance=0
        self.other_user=name
    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
    def make_deposit(self, amount):
        self.balance+=amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"{self.name} trnsfer to {other_user.name} by {amount}")
        return self
user1=User(name="Samar")
user1.make_deposit(10000).make_deposit(1000).make_withdrawal(500).display_user_balance()
