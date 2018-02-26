import urllib.request,urllib.parse,urllib.error
import re

prompt=input("Please input the site you want to be scraped: ")

html=urllib.request.urlopen(prompt).read()
match=re.findall(b'href="(.+?)"',html)
for line in match:
    print(line.decode())
    
