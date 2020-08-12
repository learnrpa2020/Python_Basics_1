def spec_func(name,*args,k=0,**kwargs):
    '''
This program has docstring so help can be used to know the fuction of the
function. Using this we can pass multiple arguments.
'''
    total=0
    for item in kwargs.values():
        total+=item
    return sum(args,total)
print(spec_func('Monica',1,2,3,4,5,n1=5,n2=10))

print('---------------------to check the functionality of the function----------')

help(spec_func)
print('--------------------------or-----------------------')
print(spec_func.__doc__)

    
