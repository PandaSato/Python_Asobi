##This is slow Algorithm!

from isPrime import isPrime 

if __name__=='__main__':
    cnt=3
    while True:
        cnt+=2
        if isPrime(cnt):
            print(cnt)
