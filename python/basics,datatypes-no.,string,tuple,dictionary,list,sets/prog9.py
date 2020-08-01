x=int(input("enter the 1st no.: "))
y=int(input("enter the 2nd no.: "))
if(x>y):
    least=y
else:
    least=x
for i in range(1,least+1):
    if((x%i==0) and (y%i==0)):
        hcf=i
print(hcf)        
        

    
