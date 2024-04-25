n=int(input())
cap,cnt=0,0
for i in range(n):
    x,y=map(int,input().split())
    cnt+=(y-x)
    cap=max(cap,cnt)
print(cap)
    