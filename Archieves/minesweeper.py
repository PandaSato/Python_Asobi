#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from MPL import *


############################Main Application#################
global W,H,M
TileSize = 15
dd = [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[1,0],[0,-1],[-1,0]]
        
class Mine():
    def __init__(self):
        self.bit = 0 # Using 4 bit to state mine
        #2^0 bit : Mine(1) NotMine(0)
        #2^1 bit : isShown(1) not Shown(0)
        #2^2 bit : isFlagged(1) not Flagged(0)
        #2^3 bit : isDoubt(1) not Doubt(0)
    def isMine(self):
        if self.bit & 1==1: return True
        return False
    def isShown(self):
        if (self.bit>>1)&1==1: return True
        return False
    def isFlagged(self):
        if (self.bit>>2)&1==1: return True
        return False
    def isDoubt(self):
        if (self.bit>>3)&1==1: return True
        return False
    def changeFlag(self):
        if self.bit&8==8: self.bit = self.bit^8
        self.bit=self.bit^4
    def changeDoubt(self):
        if self.bit&4==4: self.bit = self.bit^4
        self.bit=self.bit^8
        
class MineBoard():
    def __init__(self):
        global W,H,M
        self.mines = []
        for i in range(W*H):
            self.mines.append(Mine())
        cnt = M
        while cnt>0:
            r = random.randint(0,W*H-1)
            if self.mines[r].isMine():
                continue
            else:
                self.mines[r].bit=1 ## Make Mine
                cnt-=1
    def getMine(self,x,y):
            return self.mines[x+W*y]
    
    

class MainWindow(Genesis):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setStyleSheet("""
        QtWidget {
            background-color: rgb(0,0,0);
            color: rgb(255,255,255)
            }
        """)
        self.board = MineBoard()
        self.X=0
        self.Y=0
        self.isGameOver=False
    def initUI(self):
        self.resize(400,400)
    def drawEvent(self, event):
        self.color = 0xAA00AA
        global W,H
        for dx in range(0,W):
            for dy in range(0,H):
                self.color =0x666666
                m = self.board.getMine(dx,dy)
                if m.isMine(): self.color = 0xAAAA00
                if m.isFlagged(): self.color = 0xAA00AA
                if m.isDoubt(): self.color = 0x00AAAA                    
                if dx==self.X and dy==self.Y: self.color = 0xAA0000
                
                if m.isShown():
                    self.drawPushedSquare(5+dx*TileSize,5+dy*TileSize,TileSize)
                    self.drawNumber(dx,dy)
                else:
                    self.drawSquare(5+dx*TileSize,5+dy*TileSize,TileSize)
    def keyPressEvent(self,event):
        global W,H
        key = event.key()
        if key==Qt.Key_Up:
            self.Y-=1
        if key==Qt.Key_Down:
            self.Y+=1
        if key==Qt.Key_Left:
            self.X-=1
        if key==Qt.Key_Right:
            self.X+=1        
        if key==Qt.Key_Z:
            m = self.board.getMine(self.X,self.Y)
            if not m.isFlagged() and not m.isDoubt():
                m.bit=2 # Show
        if key==Qt.Key_X:
            m = self.board.getMine(self.X,self.Y)
            if not m.isShown():
                m.changeFlag()
        if key==Qt.Key_C:
            m = self.board.getMine(self.X,self.Y)
            if not m.isShown():
                m.changeDoubt()

            
                
        self.X = max(0,self.X)
        self.X = min(self.X,W)
        self.Y = max(0,self.Y)
        self.Y = min(self.Y,H)
    def showMineCount(self,x,y):
        global W,H
        cnt=0
        for d in dd:
            dx = d[0]+x
            dy = d[1]+y
            if 0<=dx<W and 0<=dy<H:
                if self.board.getMine(dx,dy).isMine():
                    cnt+=1
        return cnt
    def drawNumber(self,x,y):
        cnt = self.showMineCount(x,y)
        if cnt==0:
            return
        else:
            self.color=0xFFFFFF
            self.font=['Arial',12]
            self.drawBunsho(9+x*TileSize,16+y*TileSize,str(cnt))
        
if __name__ == '__main__':
    global W,H,M   
    W,H,M=10,10,20
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
