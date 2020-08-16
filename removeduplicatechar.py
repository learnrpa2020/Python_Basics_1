a='SATAAMWWE'
newstring=""
for m in a:
    #print(a[a.index(m)])
    if a[a.index(m)] not in newstring:    
        newstring = newstring+a[a.index(m)]
        print(newstring)
    
        
