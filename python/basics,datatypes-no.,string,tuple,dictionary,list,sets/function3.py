def fibonacci(rang):
    n1=0
    print(n1)
    n2=1
    print(n2)
    for i in range(1,rang+1):
        rang=n1+n2
        n1=n2
        n2=rang
        print(rang)
print(fibonacci(6))
