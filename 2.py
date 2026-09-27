#
class Dog:
    def sound(self):
        print("Dog says: Bow Bow")


class Cat:
    def sound(self):
        print("Cat says: Meow")


class Cow:
    def sound(self):
        print("Cow says: Moo")


class Lion:
    def sound(self):
        print("Lion says: Roar")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()
co = Cow()
l = Lion()

make_sound(d)
make_sound(c)
make_sound(co)
make_sound(l)