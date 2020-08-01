n=10
lim1=1
lim2=8
for _ in range(n):
    for i in range(0,lim1):
        print("*",end="")
    for j in range(lim2):
        print(" ",end="")
    for k in range(0,lim1):
        print("*",end="")
    print()
    if _<4:
        lim1=lim1+1
        lim2=lim2-2
    elif _>4:
        lim1=lim1-1
        lim2=lim2+2
