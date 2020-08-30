def newgen(num):
    for i in range(num):
        yield i

g=newgen(100)
next(g)
next(g)
print(next(g))

print('------------------------------------------------')
name= input()
password= input()

class User():
    def __init__(self,name="",password=""):
        self.name=name
        self.password=password

    def newperson(num):
        for i in range(1,num):
            yield i
            

    def login(self):
        if self.name != "" and self.password != "":
            print(f'{self.name} has logged in')
            
            
            try:
                token=input()
                m=User.newperson(100)
                while token=="next": 
                    input()
                    print(next(m))
            except:
                print("begin new session")
                
                        
                
                 
        else:
            print('login and try')
            return self


User(name,password).login()






   






