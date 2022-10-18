# Loops
for i in 'Hello World':
    print(i, end=' ')
print('\n', i)

print("\n")
for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')

print("\n")
for i in {6, 7, 8, 9, 10}:
    print(i, end=' ')

print("\n")
for i in (11, 12, 13, 14, 15):
    print(i, end=' ')

print("\n")
for i in list(range(10)):
    print(i, end=' ')
print('\n', i)

#Nested for loop
print('\nNested loop')
for item in (1,2,3,4,5,6):
    for x in ['a','b','c']:
        print(item,x)