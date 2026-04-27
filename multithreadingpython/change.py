import threading
class MyThread(threading.Thread):
    def run(self):
        print("hi",threading.current_thread().name)
th=threading.current_thread()
th.name="ram"
t=MyThread()
t.name="sita"
t.start()
print("bye",threading.current_thread().name) 