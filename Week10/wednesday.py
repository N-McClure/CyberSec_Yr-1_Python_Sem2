import threading
import time
import random

balance = 0
def withdraw_task(cond):
    global balance
    while True:
        with cond:
            time.sleep(0.5)
            print("Withdraw starting...by:", threading.currentThread().getName())
            amount = random.randint(1,10)
            while(balance < amount):
                print("Insufficient funds. Waiting for deposit...")
                cond.wait()
            balance -= amount
            print(f"Withdrawn {amount}. Current balance: {balance}")
            
def deposit_task():
    global balance
    while True:
        with cond:
            time.sleep(1)
            print("Deposit starting...")
            amount = random.randint(1,5)
            balance += amount
            print(f"Deposited {amount}. Current balance: {balance}")
            cond.notify_all()
        
if __name__ == "__main__":
    cond = threading.Condition()
    withdraw_thread = threading.Thread(target=withdraw_task, args=(cond,))
    deposit_thread = threading.Thread(target=deposit_task, args=(cond,))
    
    withdraw_thread.start()
    deposit_thread.start()
    
    withdraw_thread.join()
    deposit_thread.join()
    print("Finished Both tasks...")