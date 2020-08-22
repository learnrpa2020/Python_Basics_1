my_list=[char for char in 'hello']
print(my_list)
print('---------------------------------------------------')
my_list1=[num for num in range(0,100,3)]
print(my_list1)
print('---------------------------------------------------')
my_list2=[num**2 for num in range(50)]
print(my_list2)
print('---------------------------------------------------')
my_list3=[num**2 for num in range(50) if num**2 %2==0]
print(my_list3)

print('---------------------------------------------------')
print('---------------------------------------------------')
print('-----------------set comprehension----------------------------------')
my_set={char for char in 'hello'}
print(my_set)
print('---------------------------------------------------')
my_set1={num for num in range(0,100,3)}
print(my_set1)
print('---------------------------------------------------')
my_set2={num**2 for num in range(50)}
print(my_set2)
print('---------------------------------------------------')
my_set3={num**2 for num in range(50) if num**2 %2==0}
print(my_set3)
print('---------------------------------------------------')
print('---------------------------------------------------')
print('-----------------dictionary comprehension----------------------------------')
my_dict={
    'a':1,
    'b':2
    }
new_dict={k:v**2 for k,v in my_dict.items() if v%2==0}
print(new_dict)
