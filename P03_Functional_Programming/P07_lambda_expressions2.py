#lambda expression

my_list = [5,4,3]
new_list = list(map(lambda num:num**2,my_list))
print(new_list)
print('\n')

a = [(0, 2), (4, 4), (10, -1), (5, 3)]
a.sort()
print(a) #it sort based on the first item

a.sort(key=lambda x: x[1], reverse=True)
print(a)
a.sort(key=lambda x: x[1])
print(a)
a.sort(key=lambda x: x[1], reverse=False)
print(a)
