n=int(input())
c=list(map(int,input().split()))
c.sort(reverse=True)
s=sum(c)
st,ct=0,0
for i in c:
    st+=i
    ct+=1
    if st>s/2:
        break
print(ct)

    
    
    


