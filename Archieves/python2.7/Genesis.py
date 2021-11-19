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


#Genesis class is Base class of window. You can define your own windows as its base as Genesis.
#It has useful functions, and cleaned up messy things.

class Genesis(QWidget):
    def __init__(self):
        super(Genesis,self).__init__()
        
        ## Make UI
        self.initUI()

        ###Paint Setting
        self.painter = QPainter()
        self.color = 0xFFFFFF
        self.font = ['MS Gothic',20]
    def paintEvent(self, event):

        self.painter.begin(self)
        self.drawEvent(event) 
        self.update()        
        self.painter.end()
    
    ## Will Be Overloaded
    def initUI(self):
        return
    def drawEvent(self, event):
        return
    
    ## Painting Functions 
    def drawBunsho(self,x,y,s):
        self.painter.setPen(QColor(self.color))
        self.painter.setFont(QFont(self.font[0],self.font[1]))
        self.painter.drawText(x,y, QString(unicode(s, 'utf-8')))
    def drawYomigana(self,x,y,s):
        self.painter.setPen(QColor(self.color))
        self.painter.setFont(QFont(self.font[0],self.font[1]))
        self.painter.drawText(x,y, QString(unicode(s, 'utf-8')))        
    def drawSquare(self, x, y, size):
        
        color = QColor(self.color)
        self.painter.fillRect(x + 1, y + 1, size - 2, size - 2, color)

        self.painter.setPen(color.light())
        self.painter.drawLine(x, y + size - 1, x, y)
        self.painter.drawLine(x, y, x + size - 1, y)

        self.painter.setPen(color.dark())
        self.painter.drawLine(x + 1, y + size - 1, x + size - 1, y + size - 1)
        self.painter.drawLine(x + size - 1, y + size - 1, x + size - 1, y + 1)
class MainWindow(Genesis):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setStyleSheet("""
        QWidget {
            background-color: rgb(0,0,0);
            color: rgb(255,255,255)
            }
        """)
    def initUI(self):
        self.resize(400,400)
    def drawEvent(self, event):
        self.color = 0xFFFFFF
        self.drawBunsho(10, 50, '直接（ちょくせつ）に聞（き）いてください。')
        self.color = 0xAA00AA
        for dx in range(0,5):
            for dy in range(0,5):
                self.drawSquare(5+dx*10,60+dy*10,10)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
