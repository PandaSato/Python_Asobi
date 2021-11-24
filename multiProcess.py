## kill Python Thread after 1 second

from multiprocessing import Process
import time
import os

def f(a,b):
    cnt = 0
    while True:
        cnt+=1
        print(a**cnt+b**cnt)
        time.sleep(0.1)

if __name__ == '__main__':
    proc = Process(target=f,args=(2,3))
    startTime = time.time()
    proc.start()
    while True:
        if time.time()-startTime>1:
            print("Killed")
            proc.kill()
            break
        time.sleep(0.1)
        