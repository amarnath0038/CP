s=input()
print(["NO","YES"][any(len(k)>=7 for k in s.split("0")) or any(len(k)>=7 for k in s.split("1"))])

        
