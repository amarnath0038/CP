k,n,w=map(int,input().split())
h=int((k*w*(w+1)/2)-n)
print(["0",h][h>0])
