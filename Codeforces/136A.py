n=int(input())
k=list(map(int,input().split()))
h=[0]*n
for i in range(n):
    h[k[i]-1]=i+1
print(*h)
