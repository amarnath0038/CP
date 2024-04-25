n=int(input())
print(["NO","YES"][any(n%i==0 and set(str(i))<={"7","4"} for i in range(1,n+1))])