import threading
import time


def callback():
    for i in range(1,51):
        time.sleep(2)

def monitoring():
    for i in range(1,51):
        print(f'{i}/50') 
        time.sleep(2)

threads=[]

thread = threading.Thread(target=callback)
thread.start()
threads.append(thread)

thread_progress = threading.Thread(target=monitoring) 
thread_progress.start()
threads.append(thread_progress)

for p in threads:
    p.join()
