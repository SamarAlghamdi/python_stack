class BankAccount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance=balance
        self.int_rate=int_rate

    def deposit(self, amount):
        # your code here
        self.balance+=amount
        return self

    def withdraw(self, amount):
        # your code here
        if(self.balance>amount+5):
            self.balance-=(amount+5)
        else:
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: $"{self.balance}")
        return self

    def yield_interest(self):
        # your code here
        interst = self.int_rate * self.balance
        print(f"The yield interest is {interst}")
        return self
acount1 = BankAccount()
acount2 = BankAccount(balance=2000)

acount1.deposit(200).deposit(500).deposit(100).withdraw(250).yield_interest().display_account_info()
acount2.deposit(3000).deposit(200).withdraw(100).withdraw(50).withdraw(150).withdraw(100).yield_interest().display_account_info()


    