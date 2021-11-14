from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,time,os,random



# ex) check(QLayout,'set')
def check(*args):
    objname=args[0]
    s=""
    if len(args)>1: s=args[1]    
    l = dir(objname)
    result = []
    for line in l:
        if line.count(s)>0: result.append(line)
    return result
