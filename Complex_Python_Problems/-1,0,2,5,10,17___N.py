N=int(input())
a=-1
print(a)
for i in range(0,N):
    if(i>0):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            a=a+i
            if(a<N):
                print(a
