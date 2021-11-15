#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore

#You can import any library to libs
import sys,os

mem = '.mem'+str(231312384129435)


        
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,400)
        self.layout = QVBoxLayout()
        self.commitList=SearchList("Commits")
        self.fileList=SearchList("Files")
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
