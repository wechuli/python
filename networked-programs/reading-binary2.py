import urllib.request, urllib.response, urllib.error
data=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand=open('cover2.jpg','wb')
size=0
while True:
    info=data.read(100000)
    if len(info)<1:
        break
    size=size+len(info)
    fhand.write(info)
print(size,'characters copied')
fhand.close()
