#
class BankAccount:
    def interest(self):
        print("Bank account interest")


class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account interest: 6%")


class CurrentAccount(BankAccount):
    def interest(self):
        print("Current account interest: 2%")


s = SavingsAccount()
c = CurrentAccount()

s.interest()
c.interest()