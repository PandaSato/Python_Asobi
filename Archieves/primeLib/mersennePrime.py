import sys,os,glob,pickle
from makePrimeList import folder

def isMersennePrime(p):
    s=4
    count=0
    mod = pow(2,p)-1
    while count<p-2:
        s=pow(s,2,mod)-2
        count+=1
    if s==0:
        return True
    else:
        return False
if __name__ == '__main__':
    nums = [int(os.path.basename(x)) for x in glob.glob(folder+'/*')]
    nums.sort()
    print(nums)
    plist = pickle.load(open(folder+'/'+str(nums[0]),'rb'))
    for p in plist:
        if isMersennePrime(p):
            print("2^"+str(p)+"-1 is a Mersenne prime.")
