"""
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3) counting the
overall number of characters in the document. Don’t worry about the headers for
this exercise, simply show the first 3000 characters of the document contents.

"""
import urllib.request,urllib.error,urllib.response
import ssl

page=input("Please enter the url of the page you want to be read: ")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand=urllib.request.urlopen(page,context=ctx)
"""
try:
    fhand=urllib.request.urlopen(page,context=ctx)
except :
    print("You entered an improperly formatted url or the url you entered does not exist, the program is exiting now")
    exit()
"""
count=0
for line in fhand:
    count=count+len(line)
    if count<3000:
        print(line.decode().strip())
    
print("The web document has",count,"characters")

