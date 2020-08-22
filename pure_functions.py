from functools import reduce
my_pets=['sisi','bibi','titi','carla']
def capitalize_list(item):
    return item.capitalize()

print(list(map(capitalize_list,my_pets)))
print(my_pets)

print('--------------------------------------------------------------')
my_strings=['a','b','c','d','e']
my_numbers=[5,4,3,2,1]

print(list(zip(my_strings,sorted(my_numbers))))

print('--------------------------------------------------------------')

scores=[73,20,65,19,76,100,88]
def marks_above(item):
    return item>50
print(list(filter(marks_above,scores)))

print('--------------------------------------------------------------')
print(my_numbers+scores)
def accumulator(acc,item):
    return acc+item

print(reduce(accumulator,(my_numbers+scores),0))


