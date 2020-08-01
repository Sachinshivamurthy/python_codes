h=9
l=30
hn=0
cn=0

while(h>0):
    if(l>4):
        cn=cn+1
        l=l-4
        h=h-1
    else:
        hn=hn+1
        l=l-2
        h=h-1

print('cn',cn)
print('hn',hn)
        
