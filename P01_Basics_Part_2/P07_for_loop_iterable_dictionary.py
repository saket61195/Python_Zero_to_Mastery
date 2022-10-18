#Loop Iterable
#\n used here to look code clean
user = {
    'age': 45,
    'name': "john",
    'size': 10
}

for i in user:
    print(i,end=' ')
print('\n')

for i in user.keys():
    print(i,end=' ')
print('\n')

for i in user.values():
    print(i,end=' ')
print('\n')

for i in user.items():  # it stores each pair as tuple, in a list (in a dict_items class).
    print(i)
print('\n')

print(user.items())
print(type(user.items()))
print(list(user.items()))

for k, v in user.items():
    print(k, v)
print('\n')

for i in user.items():
    k, v = i
    print(k, v)
