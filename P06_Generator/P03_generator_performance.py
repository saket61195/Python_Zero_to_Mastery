""" from time import time


def performance(fn):
    def wrap_fn(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} sec')
    return wrap_fn


@performance
def long_fn1():
    print('1')
    for i in range(1000000):
        i*5


@performance
def long_fn2():
    print('2')
    for i in list(range(1000000)):
        i*5


long_fn1()
long_fn2()
 """

from time import time


def performance(fn):
    def wrap_fn(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} sec')
    return wrap_fn


@performance
def long_fn1():
    print('1')
    for i in range(1000000):
        yield i*5


@performance
def long_fn2():
    print('2')
    for i in list(range(1000000)):
        yield i*5


long_fn1()
long_fn2()
