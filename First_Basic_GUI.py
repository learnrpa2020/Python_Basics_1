picture =[[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]]
for i in range(len(picture)):
    for j in range(len(picture[i])):
        if picture[i][j]==1:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')


print('---------------------another smartest way------------------------------')
for i in picture:
    for j in i:
        if j:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')
