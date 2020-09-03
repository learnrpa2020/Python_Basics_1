with open('firstfile.txt',mode='r') as newfile:
    #text=newfile.write('hi')
    print(newfile.readline())


#We can change the mode 'a' to append with the file.

my_file = open('secondfile.txt')
#print(my_file.read())
print(my_file.readline(2))
#print(my_file.readlines())
my_file.close()
