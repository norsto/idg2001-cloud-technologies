from socket import *

s = socket(AF_INET, SOCK_STREAM)
# have to meke these variables..
# s.connect((HOST, PORT))
s.send(b'Hello world!')
data = s.recv()