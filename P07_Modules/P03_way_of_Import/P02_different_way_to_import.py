# import sys
# sys.path.insert(1,'/home/saket/learning/python_programming/myowncode/P07_modules/P00_main/')
# import main
# print(main)

# import sys
# sys.path.append('/home/saket/learning/python_programming/myowncode/P07_modules/')
# import P00_main.utility
# print(P00_main.utility)

# import sys
# sys.path.append('/home/saket/learning/python_programming/myowncode/P07_modules/P00_main/')
# import utility
# print(utility)


# import sys
# sys.path.append('/home/saket/learning/python_programming/myowncode/P07_modules/P01_shopping/')
# import shopping.shopping_cart
# print(shopping.shopping_cart)

# import sys
# sys.path.append('/home/saket/learning/python_programming/myowncode/P07_modules/')
# import P01_shopping.shopping.shopping_cart
# print(P01_shopping.shopping.shopping_cart)

# import sys
# sys.path.append('/home/saket/learning/python_programming/myowncode/P07_modules/')
# from P01_shopping.shopping.shopping_cart import buy
# print(buy("apple"))

# import sys
# sys.path.append('./P07_modules/')
# from P01_shopping.shopping.shopping_cart import buy
# print(buy("apple"))

# import sys
# sys.path.append('./P07_modules/')
# from P01_shopping.shopping.more_shopping.shopping_cart import buy
# from P00_main.P00_utility import divide,multipy
# print(buy("apple"))
# print(multipy(2,4))
# print(divide(25,5))


# sys.path.append('./myowncode/P07_modules/')# when myowncode is your parent directory
# one dot (.)represents the current directory that you are using
# two dot (..) represents the parent directory.
# sys.path.append('../myowncode/P07_modules/')#when myowncode is a part of subdirectory

import sys

from P00_main.P00_utility import *
from P01_shopping.shopping.more_shopping.shopping_cart import *

sys.path.append('./P07_modules/')

print(buy("apple"))
print(multipy(2, 4))
print(divide(25, 5))

# import sys
# sys.path.append('./P07_modules/')
# import P01_shopping.shopping.more_shopping.shopping_cart
# import P00_main.P00_utility
# print(P01_shopping.shopping.more_shopping.shopping_cart.buy("apple"))
# print(P00_main.P00_utility.multipy(2,4))
# print(P00_main.P00_utility.divide(25,5))


# import sys
# sys.path.append('./P07_modules/')
# import P01_shopping.shopping.more_shopping.shopping_cart as sh
# import P00_main.P00_utility as ut
# print(sh.buy("apple"))
# print(ut.multipy(2,4))
# print(ut.divide(25,5))
