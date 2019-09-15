import re

regex_url = re.compile(
    r'(https?)://www\.([A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//==]*)')
match = regex_url.search("https://www.youtube.com/blahbal?play=true")
print(match.group())
print(match.groups())


print(match.group(1))