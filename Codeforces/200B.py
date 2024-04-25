n=int(input());k=list(map(int,input().split()));s=0
for i in range(len(k)):s+=k[i]/2
print((s/(50*n))*100)
