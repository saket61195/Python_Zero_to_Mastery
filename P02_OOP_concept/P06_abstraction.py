# 4 Pillars of OPPS
# 2 -> abstraction
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
player1.run = 'boooo'# overwritten
# print(player1.run()) error
#when we call as function signature (when () not used when calling function called signature)
print(player1.run)
