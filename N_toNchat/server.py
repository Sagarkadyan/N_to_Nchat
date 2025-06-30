import socket
 
s = socket.socket()
print("socket crated")

s.bind(('localhost',5060))
s.listen(3)
print('wantion for connection ')

while True:
    c, addr = s.accept()
    print("connectd succesfully", addr)
    c.send("welcome to server")

    c.close()