#Reduce function

from functools import reduce


def accumulator(acc, item):
    # print(f'acc: {acc}, item: {item}')
    print(acc,item)
    return acc+item


my_list = [1, 2, 3, 4, 5]
# by default takes '0' as the 3rd argument
print(reduce(accumulator, my_list,0))
# print(reduce(accumulator, my_list))
print("\n")
print(reduce(accumulator, my_list, 10))
print(my_list)

'''
acc is nothing but the return of the last iteration.
'''

""" 
0 1    0+1=1
1 2    1+2=3
3 3    3+3=6
6 4    6+4=10
10 5   10+5=15
15
"""