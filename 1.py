#
class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Cash:
    def pay(self, amount):
        print("Paid", amount, "using Cash")


c = CreditCard()
u = UPI()
cash = Cash()

c.pay(1000)
u.pay(500)
cash.pay(300)