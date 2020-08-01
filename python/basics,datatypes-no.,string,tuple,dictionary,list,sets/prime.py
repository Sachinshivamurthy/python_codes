N=int(input())
for i in range(0,N):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
            
        
        
    
