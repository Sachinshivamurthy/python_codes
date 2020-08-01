x,y=map(float,input().split())
z=[]
for i in range(int(y)):
    z.append([])
    z[i]=list(map(float,input().split()))
a=list(zip(*z))
print(a)
for j in a:
    b=sum(j)/float(y)
    print("%0.1f"%b)
