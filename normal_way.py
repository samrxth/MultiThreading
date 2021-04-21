import time

timer = time.perf_counter()

def do_smt(seconds):
    time.sleep(seconds)
    print(f'Sleeping for {seconds} seconds')
    print('Done sleeping')


for _ in range(10):
    do_smt(1.5)


timer = time.perf_counter()

print(f'Done in {timer} seconds')
