import sys,os,glob,pickle
from makePrimeList import folder
if __name__ == '__main__':
    _from = int(sys.argv[1])
    _to = int(sys.argv[2])
    _from,_to = min(_from,_to),max(_from,_to)
    nums = [int(os.path.basename(x)) for x in glob.glob(folder+'/*')]
    nums.sort()
    select_from = -1
    cnt = 0
    while True:
        if _from<=nums[cnt]:
            select_from = cnt
            break
        cnt+=1
    select_to = -1
    cnt = 0
    while True:
        if _to<=nums[cnt]:
            select_to = cnt
            break
        cnt+=1
    paths = list(map(lambda x: folder+'/'+str(x),nums[select_from:select_to+1]))
    plist = [2,3]
    for path in paths:
        plist.extend(pickle.load(open(path,'rb')))
    result=[]
    for p in plist:
        if p>_to:
            break
        if _from<=p:
            result.append(p)
    print(result)
    