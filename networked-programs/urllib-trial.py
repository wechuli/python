import urllib.request

fhand=urllib.request.urlopen("http://google.com")

for line in fhand:
    print(line.decode().rstrip())
