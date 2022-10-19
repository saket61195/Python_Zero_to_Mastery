
#introspection(dir)
print(dir(list))
print("\n")
'''
It gives us all the methods and attributes that the item has access to.
But we get this functionality with IDEs build in, when we type item or instance name dot
for eg.
list.
and then IDE will pop a window with all the methods and attributes it has access to.
'''
class User():
    def __init__(self, email):
        self.email = email

    def signed_in(self):
        print("User is logged in.")

    def attack(self):
        print("Do nothing.")


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        # same as using the below command, it does not take 'self' parameter
        super().__init__(email)
        # User.__init__(self, email)

    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")


wizard1 = Wizard("John", 50, 'john@gmail.com')
print(dir(wizard1))