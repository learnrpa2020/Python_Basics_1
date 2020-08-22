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

print('-----------------------------------------------------')
user1={
    'name':'Sona',
    'valid':False
    }

def authenticated(fn):
    def wrapper(*args,**kwargs):
        if args[0]['valid']:
            return fn(*args,**kwargs)
    return wrapper

@authenticated
def message_friend(user):
    print('message is sent')

message_friend(user1)
