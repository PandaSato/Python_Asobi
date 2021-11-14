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
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.red))
        qp.setFont(QFont('Arial', 20))
        qp.drawText(10,50, QString(unicode('直接に聞いてください。', 'utf-8')))
        qp.setPen(QColor(Qt.blue))
        qp.drawLine(10,100,100,100)
        qp.drawRect(10,150,150,100)
        qp.setPen(QColor(Qt.yellow))
        qp.drawEllipse(100,50,100,50)
        qp.drawPixmap(220,10,QPixmap("python.jpg"))
        qp.fillRect(200,175,150,100,QBrush(Qt.SolidPattern))
        qp.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    display = Display()
    display.show()
    app.exec_()
