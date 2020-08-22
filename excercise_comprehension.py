some_list=['a','b','c','b','d','m','n','n']

new_list={item for item in some_list}
print(new_list)

print('-------------------------------------------------------------------')

new_list=list(set([item for item in some_list if some_list.count(item)>1]))
print(new_list)
