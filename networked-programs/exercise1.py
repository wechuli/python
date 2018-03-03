"""
Exercise 1: Change the socket program socket1.py to prompt the user for the
URL so it can read any web page. You can use split(’/’) to break the URL into
its component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user
enters an improperly formatted or non-existent URL.

"""
import socket
import re

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
page=input("Please enter the url of the page you want to be read: ")

try:
    words=page.split('/')
    hostname=words[2]
    mysock.connect((hostname,80))
    s='GET '
    s=s+page
    s=s+' HTTP/1.0\r\n\r\n'

except :
    print("You entered an improperly formatted url or the url you entered does not exist, the program is exiting now")
    exit()

mysock.send(s.encode())
while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
    
mysock.close()
print(page)



