#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore
import sys,os,time,random

libs={"QtGui":QtGui,"QtCore":QtCore}

global SelectedLibrary
        
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        global SelectedLibrary
        SelectedLibrary=QtGui
        self.initUI()
    def selectLibrary(self):
        try: 
            t = self.list1.list.currentItem()
            global SelectedLibrary
            SelectedLibrary=t.text()
            self.list2.WholeList=dir(SelectedLibrary)
            self.list2.listUpdate()
        except:
            pass
    def initUI(self):
        self.resize(800,400)
        self.layout = QHBoxLayout()
        self.list1=SearchList("Libraries")
        l = list(libs.keys())
        l.sort()
        for lib in l:
            self.list1.WholeList.append(lib)
        self.list1.listUpdate()
        self.list1.list.currentItemChanged.connect(self.selectLibrary)
        self.list2=SearchList("Classes")
        self.list3=SearchList("Components")
        
        self.layout.addWidget(self.list1)
        self.layout.addWidget(self.list2)
        self.layout.addWidget(self.list3)

        self.setLayout(self.layout)
        
            
class SearchList(QWidget):
    def listUpdate(self):
        self.list.clear()
        try:
            for k in self.WholeList:
                if k.count(self.search.text())>0:
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
