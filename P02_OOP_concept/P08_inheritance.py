# 4 Pillars of OPPS
# 3 Inheritance -> Inheritance allows us to define a class that inherits all the methods and properties from another class.

class User():
    def signed_in(self):
        print("User is logged in.")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"{self.name} is attacking with arrows : arrows left {self.num_arrows}.")

    


wizard1 = Wizard("John", 50)
archer1 = Archer("robin",100)

print(wizard1.signed_in())
print(wizard1.attack())
print(archer1.attack())

print(archer1.signed_in())
