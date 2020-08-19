class Cat:
	species='mammal'
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
cat1=Cat('Tom',5)
cat2=Cat('Mew',3)
cat3=Cat('Tim',7)		

def oldest_cat(*args):
        return max(args)
		



print(oldest_cat(cat1.age,cat2.age,cat3.age))


