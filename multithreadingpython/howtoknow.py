import threading
class MyThread(threading.Thread):
    def run(self):
        print("hi",threading.current_thread())
t=MyThread()
t.start()
print("bye",threading.current_thread())