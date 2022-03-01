import threading
import time

a=[]

def count(n):
    for i in range(0,n):
        a.append(i)
        time.sleep(0.5)

def count2(n):
    for j in range(0,n):
        a.append(j)
        time.sleep(0.5)

x = threading.Thread(target=count,args=(5,))
x.start()

y = threading.Thread(target=count2,args=(5,))
y.start()

print(threading.active_count())

x.join()
y.join()

print(a)
