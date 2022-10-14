# List Method
li = ['a', 'b', 'c', 'd', 'e', 'd']
# if that value is not there in the list, then it will throw an error and program will stop running.
print(li.index('d'))

# lookup:start:stop
print(li.index('d', 0, 5))

print('a' in li)  # we use this to avoid the error.
print('x' in li)

name = 'saket'
print('b' in name)  # we can use this with strings as well

print(li.count('d'))
