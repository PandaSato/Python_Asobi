#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from MPL import *
import sys,os,time,random,glob,pickle,numpy

libs={"QtGui":QtGui,"QtCore":QtCore, "QtWidgets":QtWidgets, "os":os,"time":time,"random":random,"glob":glob,"pickle":pickle,"numpy":numpy}

global SelectedLibrary



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        global SelectedLibrary
        SelectedLibrary=QtGui
        self.initUI()
    def getMemo(self):
        printLog(self.list3.list.currentItem().text())
    def selectLibrary(self):
        try:
            t = self.list1.list.currentItem()
            global SelectedLibrary
            SelectedLibrary=libs[str(t.text())]
            self.list2.WholeList=dir(SelectedLibrary)
            self.list2.search.setText("")
            self.list3.search.setText("")
            self.list2.listUpdate()
        except:
            pass
    def selectObject(self):
        try:
            t = self.list2.list.currentItem()
            global SelectedLibrary
            self.list3.WholeList=dir(getattr(SelectedLibrary,str(t.text())))
            self.list3.listUpdate()
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
        self.list2.list.currentItemChanged.connect(self.selectObject)        
        self.list3=SearchList("Components")
        self.list3.list.itemDoubleClicked.connect(self.getMemo)
        self.layout.addWidget(self.list1)
        self.layout.addWidget(self.list2)
        self.layout.addWidget(self.list3)

        self.mainLayout = QVBoxLayout()
        self.memoEdit = QTextEdit()
        self.mainLayout.addLayout(self.layout)
        self.mainLayout.addWidget(self.memoEdit)
        self.setLayout(self.mainLayout)
    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key_Z:
            self.memoEdit.hide()
        if event.key() == QtCore.Qt.Key_X:
            self.memoEdit.show()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
