n1=0
print(n1)
n2=1
print(n2)
n=int(input("enter the range:"))
for i in range(1,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    
