class User:
    def __init__(self,name):
        self.name =name
        self.balance=0
        self.other_user=name
    def make_withdrawal(self, amount):
        self.balance-=amount
    def make_deposit(self, amount):
        self.balance+=amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"{self.name} trnsfer to {other_user.name} by {amount}")
person1=User(name="Samar")
person1.make_deposit(10000)
person1.display_user_balance()
person1.make_withdrawal(500)
person1.display_user_balance()
person2=User(name="Nora")
person2.make_deposit(1000)
person2.display_user_balance()
person1.transfer_money(other_user=person2,amount=100)
person1.display_user_balance()
person2.display_user_balance()


        