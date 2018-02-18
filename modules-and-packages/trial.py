import django
from urllib import request

x=request.urlopen("https://www.google.com/",data=None)

print(x)