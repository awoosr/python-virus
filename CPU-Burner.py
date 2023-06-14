# CPU-Burner Virus
# By sreemanreddy
# github https://github.com/awoosr/python-virus/


from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import os

def start(x):
    timeout = time.time() + 60*1000
    while True:
        if time.time() > timeout:
            break
        x*x


processes = cpu_count()
# please be sure then clear hastags
#pool = Pool(processes)
#pool.map(start, range(processes*6))
