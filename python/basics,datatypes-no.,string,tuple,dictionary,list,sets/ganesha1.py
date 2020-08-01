def func1(int):
    for a in range(2,x+1):
        k=0
        for i in range(2,a//2+1):
            if(a%i==0):
                k=k+1
        if(k<=0):
            return(a)
x=int(input())

if(x%2==0):
    print(func1(x))
    
else:
    y1=1
    y2=1
    for i in range(1,x//2):
        y3=y1+y2
        y1=y2
        y2=y3
        
    print(y3)
    
