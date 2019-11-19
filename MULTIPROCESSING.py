import multiprocessing
import threading
import time
import os

all_process = []
processes = []

def do_another_thing(num):
    print(f"->Thread: {str(num)} computing...")
    trash = { k:k for k in range(123123) }
    trash = { k:k for k in range(123123) }
    # with thread_lock:
    print(f"->Thread: {str(num)} running...")

def do_something(num):
    
    start_time = time.time()
    t = None

    trash = sum([ x for x in range(123213) ])

    if num == 1000:
        t = threading.Thread(target=do_another_thing, args=(1000,))
        print(f"->Thread: {str(num)} start...")
        t.start()
        t.join()
        print(f"->Thread: {str(num)} end...")

    processes.append(time.time() - start_time)

    print(f"output: {str(num)} -> [start: {str(start_time)} ~ end: {str(time.time())}] -> {str(time.time() - start_time)}")
        

if __name__ == "__main__":

    thread_lock = threading.Lock()
    p = None

    for x in [1000, 5,15,20,40]:
        p = multiprocessing.Process(target=do_something, args=(x,))
        all_process.append(p)

    print(all_process)

    for x in all_process:
        x.start()
    
    for x in all_process:
        x.join()

    print(f"THREAD EXECUTION TIME TOTAL: {str(sum(processes))}")
    print(all_process)
