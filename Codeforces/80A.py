a,b=map(int,input().split());p=[]
for n in range(2,51):
    if all(n%i!=0 for i in range(2,int(n**0.5)+1)):p.append(n)
if b in p:
    print(["NO","YES"][p.index(b)==p.index(a)+1])
else:
    print("NO")
        