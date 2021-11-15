#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore

#You can import any library to libs
import sys,os

mem = '.mem'+str(231312384129435)

def dumpGit(command):
    os.system("git "+command + " > "+mem)
    f = open(mem)
    l = f.readlines()
    f.close()
    os.system("rm "+mem)
    return l
    
global commits
        
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,400)
        self.layout = QVBoxLayout()
        
        # Make Commits list
        self.commitList=SearchList("Commits")
        commit_numbers = dumpGit('log | grep commit')
        commit_dates = dumpGit('log | grep Date')
        global commits
        commits = {}
        for i in range(len(commit_dates)):
            d=commit_dates[i].rstrip().replace("Date:   ","").split("+")[0]
            commits[d]=commit_numbers[i][7:]
            self.commitList.WholeList.append(d)
        self.commitList.listUpdate()
        self.fileList=SearchList("Files")
        self.layout.addWidget(self.commitList)
        self.layout.addWidget(self.fileList)
        self.setLayout(self.layout)
        
            
class SearchList(QWidget):
    def listUpdate(self):
        self.list.clear()
        try:
            for k in self.WholeList:
                if k.upper().count(str(self.search.text()).upper())>0:
                    self.list.addItem(QListWidgetItem(k))
        except:
            pass
                
    def __init__(self,name):
        super(SearchList,self).__init__()
        self.label = QLabel(name)
        self.search = QLineEdit()
        self.search.textChanged.connect(self.listUpdate)
        self.list = QListWidget()
        self.layout = QVBoxLayout()
        self.WholeList=[]
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.list)
        self.setLayout(self.layout)
        self.listUpdate()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
