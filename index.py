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



class Genesis(QWidget):
    def __init__(self):
        super(Genesis,self).__init__()
        
        ## Make UI
        self.initUI()

        ###Paint Setting
        self.painter = QPainter()
        self.color = 0xFFFFFF
        self.font = ['MS Mincho',20]
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
        self.drawBunsho(10, 50, '直接（ちょくせつ）に聞（き）いてください。')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
