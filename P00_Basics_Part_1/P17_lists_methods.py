#List Method
print("\nappend")
li = [1, 2, 3, 4, 5]
new_li = li.append(100)
print('li = ',li)
print('new_li =',new_li)#it will print none because .append(100) add to li not new_li

new_li = li#inorder to assign/copy list of items to another items 
print('new_li =',new_li)

print("\ninsert")
new_li = li.insert(2, 2000)
print('li = ',li)
new_li = li
print('new_li =',new_li)

print("\nextend")
new_li = li.extend([45, "hello"])
print('li = ',li)
new_li = li
print('new_li =',new_li)

print("\npop")
new_li = li.pop()
print('li = ',li)
new_li = li
print('new_li =',new_li)

print("\npop")
new_li = li.pop(0)
print('li = ',li)
new_li = li
print('new_li =',new_li)

print("\nremove")
new_li = li.remove(2000)
print('li = ',li)
new_li = li
print('new_li =',new_li)

print("\nclear")
new_li = li.clear()
print('li = ',li)
new_li = li
print('new_li =',new_li)
