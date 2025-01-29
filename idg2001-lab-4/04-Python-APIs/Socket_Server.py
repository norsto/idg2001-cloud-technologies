# Server
from socket import *

s = socket(AF_INET, SOCK_STREAM)
# s.bind((HOST, PORT))  # E.g., HOST = 'localhost', PORT = 12345
s.bind(('localhost', 12345))
s.listen(1)

(conn, addr) = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)

conn.close()
