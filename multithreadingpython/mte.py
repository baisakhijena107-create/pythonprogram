import threading
import time
def display():
	for i in range (1,6):
		print("thread is runnimg:",i)
		time.sleep(1)
t1=threading.Thread(target=display)
print("main thread start")
t1.start
t1.join
print("main thread end")