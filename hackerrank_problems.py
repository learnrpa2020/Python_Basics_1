'''Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.'''

x,y,z,n=int(input('Enter the x value')),int(input('Enter the y value')),int(input('Enter the z value')),int(input('Enter the n value'))
my_list=[[i,j,k] for i in range(x+1)  for j in range(y+1)  for k in range(z+1) if i+j+k !=n]
print(my_list)
