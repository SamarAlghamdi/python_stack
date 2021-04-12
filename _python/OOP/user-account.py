from bankAccount import BankAccount
class User:
    def __init__(self,name):
        self.name =name
        self.other_user=name
        self.account=[]
    def addAccount(self,account):
        self.account.append(account)

    def make_withdrawal(self, amount,account):
        account.withdraw(amount)

    def make_deposit(self, amount,account):
        account.deposit(amount)

    def display_user_balance(self):
        print(f"User: {self.name}: ")
        for x in range(len(self.account)):
            print(f"Balance of account{x+1}: {self.account[x].balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"{self.name} trnsfer to {other_user.name} by {amount}")

person1=User(name="Sam",)
acount1 = BankAccount(int_rate=0.02, balance=1000)
acount2 = BankAccount(balance=2000)
person1.addAccount(acount1)
person1.addAccount(acount2)

person1.make_deposit(10000,acount1)
person1.display_user_balance()
person1.make_withdrawal(500,acount1)
person1.display_user_balance()
# person2=User(name="Nora")
# person2.make_deposit(1000,acount1)
# person2.display_user_balance()
# person1.transfer_money(other_user=person2,amount=100)
# person1.display_user_balance()
# person2.display_user_balance()


        