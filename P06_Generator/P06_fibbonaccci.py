
#generator
def fib(number):
    n1 =0
    n2 =1
    for i in range(number):
        yield n1  
        n3=n2+n1
        n1=n2
        n2=n3
        

for x in fib(10):
    print(x,end =' ')


""" #generator
def fib(number):
    n1 =0
    n2 =1
    for i in range(number):
        yield n1  
        temp=n1
        n1=n2
        n2=temp + n2

for x in fib(10):
    print(x,end=' ') """

""" #using list
def fib(number):
    n1 =0
    n2 =1
    result = []
    for i in range(number):
        result.append(n1) 
        n3=n2+n1
        n1=n2
        n2=n3
    return result

print(fib(10)) """
# print('hello'[0])
# print('hello'.sub(0,1))
# print(sub('hello',0,1))