fhand=open("prog1.txt")
print(fhand)
count=0
for line in fhand:
    count=count+1
    if(line.startswith("py")):
        print(line)
print(count)
print(fhand.read())
#print(inp)

