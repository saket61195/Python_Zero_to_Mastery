

class PlayerCharacter:
    # Class object attribute, its an attribute of PlayerCharacter. It is a static attribute
    membership = True

    def __init__(self, name, age):
        if self.membership:    # or we can write: 'if PlayerCharacter.membership :'
            self.name = name  # these are dynamic attribute
            self.age = age

    def run(self):
        print(f"run {self.name}")
        # print(f"run {PlayerCharacter.name})   # we cannot do this


player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)

print(player1.name)
# each of the class instace can assess the class object attribute
print(player1.membership)
print(player1.run())
