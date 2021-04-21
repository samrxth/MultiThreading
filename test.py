import threading
import time

timer = time.perf_counter()

def do_smt(seconds):
    time.sleep(seconds)
    print(f'Sleeping for {seconds} seconds')
    print('Done sleeping')


threads = []

for _ in range(10):
    thread = threading.Thread(target=do_smt, args=[1.5])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

timer = time.perf_counter()

print(f'Done in {timer} seconds')
