lis=[(1,3),(2,5),(4,8),(9,10),(5,6),(4,7),(7,10)]
lis1=[0 for k in range(32)]
for i in lis:
    for j in range(i[0],i[1]+1):
        lis1[j]=lis1[j]+1
date=lis1.index(max(lis1))
print(date)
