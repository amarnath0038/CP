n=int(input());a=[];b=[];c1,c2=0,0
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
s="".join(map(str,a));k="".join(map(str,b))
if s.count("1")>s.count("0"):c1=s.count("0")
else:c1=s.count("1")
if k.count("1")>k.count("0"):c2=k.count("0")
else:c2=k.count("1")
print(c1+c2)


    
    
    