import urllib.request, urllib.response, urllib.error
data=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand=open('cover.jpg','wb')
fhand.write(data)
fhand.close()