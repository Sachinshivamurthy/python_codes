import urllib.request 
from bs4 import BeautifulSoup
req = urllib.request.Request( "http://www.team4adventure.com/tours", data=None, 
             headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' } 
                                      ) 
f = urllib.request.urlopen(req) 
s=f.read()

soup=BeautifulSoup(s)
a=soup.find(class_='tour-card-name')
link=a.find_all('a')
for l in link:
        names = l.contents[0]
        links = l.get('href')
        print(links)
        print(names)
'''text=soup.get_text()
print(text)
lines=(line.strip() for line in text.splitlines())

for line in lines:
	print(line)'''
