#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

# 자동완성을 위해서 만들어놓은 오브젝트 리스트들..
# 실제로 쓸 필요는 없음.
QtObjList = [QWidget, 
             QVBoxLayout, QGridLayout,
             QLineEdit,QPushButton,QTextEdit,QTextBrowser]
#test



class Display(QWidget):
    def __init__(self):
        super(Display,self).__init__()
        
        ## Make UI
        self.resize(400,400)
        self.layout = QVBoxLayout()
        self.example = QLineEdit("Hello World")
        self.button = QPushButton("Hello World!")
        self.layout.addWidget(self.example)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    display = Display()
    display.show()
    app.exec_()
