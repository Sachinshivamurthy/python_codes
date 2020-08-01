def nsum(n):
    sum=0
    if(n<1):
        return n
    else:
        for i in range(1,1+n):
            sum=sum+i
        return sum
print(nsum(5))
    
            
