#generate a number 1-10
#input from user?
#check that input is a number 1-10
#check if number is the right guess. otherwise ask again

# from random import randint
# answer = randint(1,10)

# while True:
#     try:
#         print(answer)
#         guess = int(input('Guess a number 1-10: '))
#         if guess > 0  and guess < 11:
#         # if  0 < int(guess) < 11:
#             # print('all good')
#             if guess == answer:
#                 print("you are genius!")
#                 break
#         else:
#             print("out of bound")
#     except ValueError:
#         print('Please enter a number ') 
#         continue

import sys
from random import randint
answer = randint(int(sys.argv[1]),int(sys.argv[2]))

while True:
    try:
        print(answer)
        guess = int(input(f'Guess a number {sys.argv[1]}-{sys.argv[2]}: '))
        if guess > 0  and guess < 11:
        # if  0 < int(guess) < 11:
            # print('all good')
            if guess == answer:
                print("you are genius!")
                break
        else:
            print("out of bound")
    except ValueError:
        print('Please enter a number ') 
        continue



