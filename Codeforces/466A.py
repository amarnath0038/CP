n,m,a,b=map(int,input().split())
print([n*a,(n//m)*b+min(b,(n%m)*a)][m*a>b])
        

    
    

