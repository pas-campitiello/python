class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r,"+ (", x.i,")*i")

print("-------------------------------")

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)               # shared by all dogs
print(e.kind)               # shared by all dogs
print(d.name)               # unique to d
print(e.name)               # unique to e

d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
