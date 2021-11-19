#My Python Libraries(MPL)

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore
import sys,os


# ListWidget with search window!
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