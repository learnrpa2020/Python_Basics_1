from time import time


def performance(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result=fn(*args,**kwargs)
        t2=time()
        print(f'took{t2-t1} s')
        return result
    return wrapper






@performance
def long_time():
    for i in range(10000):
        i*5


@performance
def long_time2():
    for i in range(100000000):
        i*5
        
long_time()
long_time2()
