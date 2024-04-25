n=int(input());k=list(map(int,input().split()))
t=k.index(max(k))+k[::-1].index(min(k))
print([t-1,t][t<n])
