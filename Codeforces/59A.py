s=input()
c1,c2=0,0
for i in range(len(s)):
    if 97<=ord(s[i])<=122:
        c1+=1
    else:
        c2+=1
if c1>=c2:
    print(s.lower())
else :
    print(s.upper())

    
    
    
