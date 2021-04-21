import concurrent.futures as conc_f
import time


timer = time.perf_counter()


def do_smt(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"Done sleeping for {seconds}"


with conc_f.ThreadPoolExecutor() as executor:
    secs = range(1,6)
    threads = [executor.submit(do_smt, sec) for sec in secs]

    for thread in threads:
        print(thread.result())

timer = time.perf_counter()
print(f'Done in {timer} seconds')
