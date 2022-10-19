
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(super_list1)

super_list1.append(0)
super_list1.append(100)
print(super_list1)

print(len(super_list1))

print(issubclass(SuperList, list))
print(issubclass(list, object))
print(issubclass(SuperList, object))
