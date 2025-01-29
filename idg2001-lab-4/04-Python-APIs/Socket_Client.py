# Client
from socket import *

s = socket(AF_INET, SOCK_STREAM)
# s.connect((HOST, PORT))  # E.g., HOST = 'localhost', PORT = 12345
s.connect(('localhost', 12345))
s.send(b'Hello, world!')
data = s.recv(1024)
print(data)
s.close()
