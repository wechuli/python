"""
Exercise 2: Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of
characters and display the count of the number of characters at the end of the
document.

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
count=0
while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    count=count+len(data)
    if count<3000:    
        print(data.decode(),end='')
    
    
mysock.close()
print(page)
print(count)

#I can't solve this, the program above should work, but it aint


