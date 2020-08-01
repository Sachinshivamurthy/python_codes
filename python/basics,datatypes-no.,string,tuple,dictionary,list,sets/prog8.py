x=int(input("enter the 1st number: "))
y=int(input("enter the 2nd number: "))
true=0
if(x>y):
    greater=x
else:
    greater=y
    while(true==0):
        if((greater%x==0 ) and (greater%y==0)):
            print(greater)
            break
        greater=greater+1
