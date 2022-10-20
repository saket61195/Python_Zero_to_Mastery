#Find duplicate using comprehension

some_list = ['a','b','c','b','d','m','n','m']

duplicate_list = list(x for x in some_list if some_list.count(x)>1)
print(duplicate_list)
duplicate_list1 = list(set(x for x in some_list if some_list.count(x)>1))
print(duplicate_list1)
duplicate_list2 = set([x for x in some_list if some_list.count(x)>1])
print(duplicate_list2)