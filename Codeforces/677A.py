n,h=map(int,input().split());c=0
a=list(map(int,(input().split())))
for i in range(len(a)):
    if int(a[i])>h:
        c+=1
print((c*2)+(n-c))
        