n,k=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(n):
    if l[i]>=l[k-1] and l[i]!=0:
        p+=1
print(p)