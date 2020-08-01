import re
result=re.search('niit','iit python class niit')
print(result)
x='all is well eat  xyz sleep earth ascii example optimus prime'
result1=re.findall("[^a]\w*",x)
print(result1)
y=((re.split(r"\s","we are splitting the words")))
z=re.match("^s",y)
