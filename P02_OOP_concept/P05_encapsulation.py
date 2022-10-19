# 4 Pillars of OPPS

#1 -> Encapsulation
#It describes the idea of wrapping data and the methods that work on data within one unit

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name    # Attribute or Property
        self.age = age
        print("I get printed at every instance created")

    def run(self):
        print("run method")


player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)
print(player1.run())
