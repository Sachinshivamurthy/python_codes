num=int(input("enter the number:"))
b,c=divmod(num,5)
if(c==0):
    print("number is divisible by 5")
    a=num*num
    print("area of square:",a)
else:
    print("not divisible")
