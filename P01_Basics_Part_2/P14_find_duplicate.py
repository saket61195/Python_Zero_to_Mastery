some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates) #it will print only duplicate item


duplicates1 = []
for value in some_list:
        if value not in duplicates1:
            duplicates1.append(value)
print(duplicates1) #it will remove duplication