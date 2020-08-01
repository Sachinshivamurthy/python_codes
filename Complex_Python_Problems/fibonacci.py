#fibonacci series for a given Range
n=int(input())
a=0
b=1
while(a<n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#Sum of fibonacci series
n=int(input())
a=0
b=1
while(a<n):
    c=a+b
    a=b
    b=c
print(c-1)
