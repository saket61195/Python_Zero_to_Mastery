
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

print(isinstance(wizard1, Wizard))
#wizard1 is instance of wizard
print(isinstance(wizard1, User))
#wizard class is sub class of User
print(isinstance(wizard1, object))
#in python every thing is object so it inherit from base call "object"
print(isinstance(wizard1, Archer))

'''
By default every class is a subclass of 'object' class, hence when we type 'instance.' (object_name dot), we get all those
defualt methods suggestions from the IDE.
'''
