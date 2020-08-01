lis=[(1,2),(2,3),(3,2),(1,3),(4,3),(5,3),(6,2),(7,3),(8,2),(9,3),(10,1),(11,4),(12,4)]
lis1=[]
lis2=[0 for k in range(8)]
for i in lis:
    if i[0] not in lis1:
        lis1.append(i[0])
    else:
        print("Fraud Voter ID:",i[0])
    j=i[1]
    lis2[j]=lis2[j]+1
print("canID:",end=' ')
for k in range(3):
    canID=lis2.index(max(lis2))
    print(canID,end=' ')
    lis2[canID]=0
