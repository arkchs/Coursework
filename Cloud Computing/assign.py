import threading
import time


def worker1():
    i=1
    while i<11:
        print(i)
        time.sleep(1)
        i+=1

thread1 = threading.Thread(target=worker1)
thread2 = threading.Thread(target=worker1)




thread1.start()
thread2.start()