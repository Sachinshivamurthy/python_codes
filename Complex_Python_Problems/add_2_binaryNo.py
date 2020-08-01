def B_D(a):
    b=0
    i=0
    while(a>0):
        n=a%10
        b=b+n*(2**i)
        a=a//10
        i=i+1
    return b
def D_B(x):
    y=0
    i=0
    while(x>0):
        n=x%2
        y=y*10+n
        x=x//2
    return y    
a=B_D(int(input()))
b=B_D(int(input()))
c=a+b
d=D_B(c)
print(d)


    
