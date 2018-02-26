import urllib.request
import re

fhand=urllib.request.urlopen("http://mozilla-splash-page20180216122052.azurewebsites.net/")
for line in fhand:
    line=line.strip().decode()
    match=re.findall(b'"href=(.+?)"',line)

print(match)
