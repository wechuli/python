"""
Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
tags from the retrieved HTML document and display the count of the paragraphs
as the output of your program. Do not display the paragraph text, only count
them. Test your program on several small web pages as well as some larger web
pages.
"""
from bs4 import BeautifulSoup
import urllib.request,urllib.response,urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

page=input("Please enter the page you want opened: ")
html=urllib.request.urlopen(page,context=ctx).read()

soup=BeautifulSoup(html,'html5lib')
para=soup.find_all('div')

print(soup.prettify())
#print(para)

print(len(para))