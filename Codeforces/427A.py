n=int(input())
events=list(map(int,input().split()))
un_crs=of_av=0
for event in events:
    if event==-1:
        if of_av>0:
            of_av-=1
        else:
            un_crs+=1
    else:
        of_av=of_av+event
print(un_crs)
            
        
        
    
        