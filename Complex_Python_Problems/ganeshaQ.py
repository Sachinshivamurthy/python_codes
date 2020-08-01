x=[1,2,1,1,1]        #delhi ganesha interview Q 
y=len(x)             #[1,2,1,0,0]
i=0                  #[1,3,1,2,0,1]
j=True
while(j):
    if(x[i]==0):
        print('false')
        break
    if(i == (y-1)):
        print('true')
        break
    k=1
    while(k<x[i]):
        if(x[i]+x[i+k]==y-1):
            i=i+x[k]
            break
        k=k+1
    else:    
        i=i+x[i]
else:
    print('false')
