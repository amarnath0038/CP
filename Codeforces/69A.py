n=int(input())  
sx=sy=sz=0
for i in range(n):
    x,y,z=map(int, input().split())
    sx+=x;sy+=y;sz+=z
print(["NO","YES"][sx==0 and sy==0 and sz==0])
    
    