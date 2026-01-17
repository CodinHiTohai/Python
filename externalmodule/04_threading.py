import threading
import time
def worker(num):
    print(f"Thread{num}:starting")
    time.sleep(2)
    print(f"Thread{num}:finishind")


    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
            thread.join()  # Wait for all threads to finish
 
print("All threads completed.")