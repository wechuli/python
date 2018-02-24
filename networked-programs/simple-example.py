import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('mozilla-splash-page20180216122052.azurewebsites.net', 80))
cmd = 'GET http://mozilla-splash-page20180216122052.azurewebsites.net/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
    
mysock.close()