# Positional Parameters
def say_hello(name, age):
    print(f'Hi {name}, your age is {age}')

# Default Parameters


def say_hello2(name="jojo", age=25):
    print(f'Hi {name}, your age is {age}')


# Positional Arguments
say_hello("saket", 27)

# Default Arguments
say_hello2()
say_hello2("saket")

# Key Arguments
say_hello(age=89, name="Andrei")
