def GetSubset(Input1, Input2):
    lent=len(Input1)//2
    com=[]
    for i in Input1:
        count=0
        for j in Input1:
            if i>j:
                count+=1
        com.append(count)  
    emp=[]
    for i in range(len(Input1)):
        for j in range(i+1,len(Input1)):
            new=[]
            if(Input1[i]+Input1[j]==Input2 and (com[i]>lent or com[j]>lent)):
                new.append(Input1[i])
                new.append(Input1[j])
                emp.append(new)
    return emp

print(GetSubset([1,3,5,10,12], 15))
