import time
import threading

def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task finish")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task finish")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All task complete")
