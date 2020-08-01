def prime(n):
    for j in range(2,n):
        if(n%j==0):
            break
    else:
        return("True")
    return("False")
n=int(input())
print(prime(n))

