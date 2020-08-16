'''
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


n=int(input('Enter the number'))
if n%2 != 0:
    print('Weird')
else:
    if n in range(2,6):
        print('Not Weird')
    elif n in range(6,21):
        print('Weird')
    else:
        print('Not Weird')


'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.'''


word=input('Enter the word')
a=len(word)
li =[]
li1=[]
stuart=0
kevin=0
for i in range(a+1):
    for j in range(a+1):
        if i!=j and j>i:
            if word[i][0] in ['A','E','I','O','U']:
                li.append(word[i:j:])
                kevin=len(li)
            else:
                li1.append(word[i:j:])
                stuart=len(li1)
                
print(kevin)
print(stuart)

word1=input('enter the word')
k=int(input('enter the num'))
n=len(word1)
li3=[]
q=int(n/k)
for t in range(0,n,k):
    li3.append(word1[t:k+t:])
m=0
newstring=""
for item in li3:
    for m in range(k):
        if item[m] not in newstring :
            newstring=newstring+item[m]
print(newstring)
    
    
    
       
        
        
    
    
    
    
    
    
        

    
    
    



