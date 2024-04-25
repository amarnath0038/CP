n=input();m=input();s=[]
for i in range(len(n)):
    if n[i]==m[i]:
        s.append("0")
    else:
        s.append("1")
print(''.join(s))

    