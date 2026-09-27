#
class Food:
    def prepare(self):
        print("Preparing food")


class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger")


class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani")


def order(food):
    food.prepare()


p = Pizza()
b = Burger()
bir = Biryani()

order(p)
order(b)
order(bir)