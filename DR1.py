import threading
# Савісько Андрій КІ-33

def thread1():
    print("Thread 1 is running")
    for i in range(100):
        print(f"Thread 1: {i}")
    
def thread2():
    print("Thread 2 is running")
    for i in range(100):
        print(f"Thread 2: {i}")  
 
print("Main thread is running")   
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
