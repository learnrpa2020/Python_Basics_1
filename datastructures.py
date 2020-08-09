name='MONICA'
name.lower()
print(name.lower())

print('----------------------------------------------------------')
print('Enter the products')
amazon_products=[]
amazon_products_len =5
for i in range(amazon_products_len):
    
    #value=input()
    amazon_products.insert(i,input())
    i=+1
    #print(amazon_products)
print(amazon_products)

print('----------------------------------------------------------')
print('Enter the products')
amazon_products={}
amazon_products_len =5
for i in range(amazon_products_len):
    key = input()
    value = int(input())
    amazon_products.update({key:value})
    i=+1
print(amazon_products)
print(amazon_products.items())
print(amazon_products.keys())
print('Apple' in amazon_products)
print('----------------------------------------------------------')
amazon_products=(1,2,3,4,5)
print(amazon_products)
