m=[list(map(int,input().split())) for i in range(5)]
r,c=0,0
for i in range(5):
    if 1 in m[i]:
        r,c=i,m[i].index(1)
print(abs(r-2)+abs(c-2))
