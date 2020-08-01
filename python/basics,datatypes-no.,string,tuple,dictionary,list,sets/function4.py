def palindrome(n):
    x=n
    r=0
    while(n>0):
        dig=n%10
        r=r*10+dig
        n=n//10
    if(r==x):
        return 1
    else:
        return 0
print(palindrome(37))
