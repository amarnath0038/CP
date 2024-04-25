n=int(input());k=list(map(int,input().split()));cnt=0  
for i in range(1,n):
    if k[i]<min(k[0:i]) or k[i]>max(k[0:i]):cnt+=1
print(cnt)
    