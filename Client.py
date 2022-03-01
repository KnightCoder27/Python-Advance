import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((socket.gethostname(),1024))
msg = soc.recv(127)
print(msg.decode("utf-8"))
