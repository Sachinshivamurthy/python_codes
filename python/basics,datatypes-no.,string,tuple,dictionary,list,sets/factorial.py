num=int(input("enter a positive no:"))
fact=1
if(num==0):
    print("factorial is:",fact)
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial is:",fact)    
