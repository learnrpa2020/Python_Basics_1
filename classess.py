firstname = input()
lastname = input()
class User():
   
    def __init__(self,firstname,lastname):
        self.firstname =firstname
        self.lastname=lastname


    def fullname(self):
        print(self.firstname + self.lastname)
        return self


User(firstname,lastname).fullname()
print(__name__)



