import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((socket.gethostname(),1024))
soc.listen(5)

while True:
        clt,addr = soc.accept()
        print(f"Connection Estabish to Address {addr}")
        msg = "Message received and the message is "
        clt.send(bytes(msg+" Network Programming using Python ", "utf-8"))
