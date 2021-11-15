from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore
import sys,time,os,random


libs=[QtGui,QtCore,sys,os]
global lib,obj

def clear():
    os.system('clear')
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

def getLibrary():
    while True:
        clear()
        print("libs="+str(str(libs).split("\'")[1::4]))
        print("please input number from 0~")
        n = raw_input()
        try:
            if 0<=int(n)<len(libs):
                lib=libs[int(n)]
                return lib
        except:
            pass
        
def getObject():
    global lib
    s=""
    while True:
        clear()
        Objs = dir(lib)
        result = []
        for obj in Objs:
            if obj.upper().count(s.upper())>0:
                result.append(obj)
        for obj in result: print(obj)
        s = raw_input("please input(-1=back, 1=select): ")
        if s=='-1':
            lib=getLibrary()
            s=""
        elif s=='1':
            if len(result)>0:
                return getattr(lib,result[0])
            else:
                s=''
                
def checkMethod():
    global obj
    s=""
    while True:
        clear()
        Ms = dir(obj)
        result = []
        for m in Ms:
            if m.upper().count(s.upper())>0:
                result.append(m)
        for m in result: print(m)
        s = raw_input("please input(-1=back):")
        if s=='-1':
            obj=getObject()


def main():
    global lib,obj
    lib=getLibrary()
    obj=getObject()
    checkMethod()

    
if __name__ == "__main__":
    main()

