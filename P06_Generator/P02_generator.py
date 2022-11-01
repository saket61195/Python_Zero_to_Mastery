
def generator_fun(num):
    for i in range(num):#0 1 2 3 4 5
        yield i*2

g = generator_fun(6)
# g = generator_fun(5) #StopIteration we cant do next after 5 so stop iteration
print(next(g))#0*2=0
next(g)#1*2=2
next(g)#2*2=4
print(next(g))#2*3=6
next(g)#2*4=8
print(next(g))#2*5=10

#yield keyword paused the function operation and run one by one
#next is used to run generator one by one