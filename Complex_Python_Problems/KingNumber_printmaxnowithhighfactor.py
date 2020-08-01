x=[2,3,5,6,9,14,20]
y=[]
for i in x:
    for l in range(2,i):
        if(i%l==0):
            break
        else:
            y.append(i)
print(y)





''' k=0
            for j in x:
                if j%i==0:
                    k+=1
            y.append(k)
print(y)
l=y.index(max(y))
print(x[l])
'''
