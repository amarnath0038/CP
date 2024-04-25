n=int(input())
count=0
for i in range(n):
    s=list(map(int,input().split()))
    if s.count(1)>=2:
       count+=1
print(count)
