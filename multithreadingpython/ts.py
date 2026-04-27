# Thread Synchronization Bank Program in Python

import threading
import time

class Bank:
    def __init__(self):
        self.balance = 1000   # Initial Balance
        self.lock = threading.Lock()   # Lock for synchronization

    def deposit(self):
        for i in range(3):
            amt = int(input("Enter deposit amount: "))
            
            self.lock.acquire()   # Lock start
            self.balance = self.balance + amt
            print("Deposited:", amt)
            print("Current Balance:", self.balance)
            self.lock.release()   # Lock end
            
            time.sleep(1)

    def withdraw(self):
        for i in range(3):
            amt = int(input("Enter withdraw amount: "))
            
            self.lock.acquire()   # Lock start
            if amt <= self.balance:
                self.balance = self.balance - amt
                print("Withdrawn:", amt)
            else:
                print("Insufficient Balance")
            print("Current Balance:", self.balance)
            self.lock.release()   # Lock end
            
            time.sleep(1)

# Object creation
b = Bank()

# Creating threads
t1 = threading.Thread(target=b.deposit)
t2 = threading.Thread(target=b.withdraw)

print("Bank Transaction Started")

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Final Balance:", b.balance)
print("Bank Transaction Completed")