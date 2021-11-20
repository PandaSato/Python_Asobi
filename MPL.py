## My Python Library

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random,time

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
        self.painter.drawText(x,y, s)
    def drawYomigana(self,x,y,s): ## Ima working-chu
        self.painter.setPen(QColor(self.color))
        self.painter.setFont(QFont(self.font[0],self.font[1]))
        self.painter.drawText(x,y, s)        
    def drawSquare(self, x, y, size):
        
        color = QColor(self.color)
        self.painter.fillRect(x + 1, y + 1, size - 2, size - 2, color)

        self.painter.setPen(color.lighter())
        self.painter.drawLine(x, y + size - 1, x, y)
        self.painter.drawLine(x, y, x + size - 1, y)

        self.painter.setPen(color.darker())
        self.painter.drawLine(x + 1, y + size - 1, x + size - 1, y + size - 1)
        self.painter.drawLine(x + size - 1, y + size - 1, x + size - 1, y + 1)
    def drawPushedSquare(self, x, y, size):
        
        color = QColor(self.color)
        self.painter.fillRect(x + 1, y + 1, size - 2, size - 2, color)

        self.painter.setPen(color.darker())
        self.painter.drawLine(x, y + size - 1, x, y)
        self.painter.drawLine(x, y, x + size - 1, y)

        self.painter.setPen(color.lighter())
        self.painter.drawLine(x + 1, y + size - 1, x + size - 1, y + size - 1)
        self.painter.drawLine(x + size - 1, y + size - 1, x + size - 1, y + 1)