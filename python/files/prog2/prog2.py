fhand=open("prog2.txt")
for line in fhand:
    if line.find("@gmail.com"):
         print(line+"xyz")
print(fhand.read( ))
    #print(p)
