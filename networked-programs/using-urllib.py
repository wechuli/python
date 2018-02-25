import urllib.request
fhand=urllib.request.urlopen('http://mozilla-splash-page20180216122052.azurewebsites.net/')
for line in fhand:
    print(line.decode().strip())
