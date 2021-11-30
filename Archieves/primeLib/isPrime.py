
from makePrimeList import folder
import sys,glob,os,pickle

def isPrime(p):
    sqrt = int(pow(p,0.5))
    for n in range(2,sqrt):
        if p%n==0:            
            return False
    return True
if __name__=='__main__':
    p = int(sys.argv[1])
    nums = [int(os.path.basename(x)) for x in glob.glob(folder+'/*')]
    nums.sort()
    select = ''
    for num in nums:
        if p<=num:
            select = folder+'/'+str(num)
            break
    if select=='':
        #print(str(p) + ' is too big')
        if isPrime(p):
            print(str(p)+' is a prime')
        else:
            print(str(p)+' is not a prime')            
        sys.exit()
    file = open(select,'rb')
    plist = [2,3]+pickle.load(file)
    if p in plist:
        print(str(p) + ' is a prime')
    else:
        print(str(p) + ' is not a prime')
    
