amazon_products ={'Apple':20,'Banana':30,'Kiwi':60,'Cherry':90,'Mango':15}
print('Enter the fruit u want')
value = input()
print(value in amazon_products)
if value in amazon_products:
    amount=amazon_products.get(value)
    print(amount)
print('using ternary operator')
print(amazon_products.get(value)) if value in amazon_products else print("Product not available")

print('----------------Truthy Falsy-----------')

username=input('Enter the username')
password=input('Enter the password')
if username and password:
    print('You have successfully logged in-Truthy')
elif not(username):
    print('You are not entered the username -Falsy')
elif not(password):
    print('You are not entered the password -Falsy')
else:
    print('You are not entered the username and password -Falsy')

print('----------------Truthy Falsy using ternary operator-----------')
print('You have successfully logged in-Truthy') if username and password else print('You are not entered the username or password -Falsy')
