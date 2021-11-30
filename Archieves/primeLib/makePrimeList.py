import pickle,os,glob
folder = 'PrimeNumbers'


##Using plist(prime List), from sp(start Prime), make new Prime List that has length of cnt(count)
def makePrimeList(plist, sp, cnt):
    
    ##initialization

    if plist==[]:
        plist=[2]
    new_plist = []
    if sp<=1:
        new_plist.append(2)
    sp = max(1,sp)
    if sp%2==0:
        sp+=1
    
    #make new prime list
    while cnt>0:
        sp+=2
        sqrt = pow(sp,0.5)
        isPrime = True
        for p in plist:
            if p>sqrt:
                break
            if sp%p==0:
                isPrime = False
                break
        if isPrime:
            plist.append(sp)
            new_plist.append(sp)
            cnt-=1
    return new_plist


        
if __name__=='__main__':
    
    ##initialize prime list
    if len(glob.glob(folder))==0:
        os.system("mkdir "+folder)
    plist=[2,3]
    names = glob.glob(folder+'/*')
    names.sort(key = lambda x: int(os.path.basename(x)))
    for primefile in names:
        plist+=pickle.load(open(primefile,'rb'))
    
    while True:
        list = makePrimeList(plist,plist[-1],100000)
        name = list[-1]
        path = folder+'/'+str(name)
        os.system('touch '+path)
        file = open(path,'wb')
        pickle.dump(list,file)
        print("made prime list ~"+str(name))