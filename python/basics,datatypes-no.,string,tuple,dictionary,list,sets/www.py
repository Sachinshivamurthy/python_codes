n="python is program"
y=len(n)
x=n[0]
print(x)
for i in n[1:y+1]:
    if(i!="p"):
        print(i)
    elif(n.startswith("pyt")):
        i="$"
        print(i)
    else:
        i=""
        print(i)
