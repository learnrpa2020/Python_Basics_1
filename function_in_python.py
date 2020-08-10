def checkDriverAge():
    print('Enter your age')
    age= int(input())
    if age> 18:
      output= 'Powering on the car!!!!'
    elif age < 18:
        output='u are not old enogh to drive'
    elif age == 18:
       output ='welcome to the first year of riding'
    return print(output)


checkDriverAge()

print('-----program will take the default value if it is not passed an argument--------------------------------------')

def checkDriverAge(age=0):
    if age> 18:
      output= 'Powering on the car!!!!'
    elif age < 18:
        output='u are not old enogh to drive'
    elif age == 18:
       output ='welcome to the first year of riding'
    return print(f'{output} because u r {age} years old')

checkDriverAge()
    


    

    



    
