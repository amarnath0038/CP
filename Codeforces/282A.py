x=0
for i in range(int(input())):
    s=input()
    if s.count("+")==2:
        x+=1
    else:
        x-=1
print(x)