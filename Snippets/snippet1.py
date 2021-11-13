from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,time,os,random



##특정 객체명이 가지고 있는 메소드 혹은 요소를 찾아본다.
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
