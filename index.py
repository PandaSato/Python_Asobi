#!/usr/bin/python
# -*- coding: utf-8 -*-
# QTableWidget Example @pythonspot.com
from MPL import *

#You can import any library to libs
import sys,os,glob

mem = '.mem'+str(231312384129435)

def dumpGit(command):
    os.system("git "+command + " > "+mem)
    f = open(mem)
    l = f.readlines()
    f.close()
    os.system("rm "+mem)
    return l
    
global commits
        
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()
        
    def getChangedFiles(self):
        try:
            global commits
            selectedCommits = self.commitList.list.selectedItems()
            if len(selectedCommits)==1:
                self.fileList.WholeList=[]
                from_commit = commits[str(selectedCommits[0].text())]
                to_commit =commits[str(self.commitList.list.currentItem().text())]
                result = dumpGit('diff --name-only '+from_commit+' '+to_commit)
                for f in result:
                    if f.rstrip()[-3:]=='.py':
                        self.fileList.WholeList.append(f.rstrip())
                self.fileList.listUpdate()
            if len(selectedCommits)>=2:
                self.commitList.list.clearSelection()
        except:            
            pass
            
    def getHistory(self):
        try:
            selectedCommits = self.commitList.list.selectedItems()
            from_commit = commits[str(selectedCommits[0].text())]
            to_commit =commits[str(selectedCommits[1].text())]
            result = dumpGit('diff '+from_commit+' '+to_commit+' '+str(self.fileList.list.currentItem().text()))
            self.HistoryViewer.setPlainText("")
            for line in result:
                if line[0]=='+': self.HistoryViewer.setTextBackgroundColor(QColor(0xAAFFAA))
                elif line[0]=='-': self.HistoryViewer.setTextBackgroundColor(QColor(0xFFAAAA))
                else: self.HistoryViewer.setTextBackgroundColor(QColor(0xFFFFFF))
                self.HistoryViewer.insertPlainText(line)
        except:
            pass
            

    def initUI(self):
        self.resize(800,600)
        self.layout = QVBoxLayout()
        
        # Make Commits list
        self.commitList=SearchList("Commits")
        self.commitList.list.setSelectionMode(QListWidget.MultiSelection)
        self.commitList.list.currentItemChanged.connect(self.getChangedFiles)
        commit_numbers = dumpGit('log | grep commit')
        commit_dates = dumpGit('log | grep Date')
        commit_comments = dumpGit('log --oneline')
        global commits
        commits = {}
        for i in range(len(commit_dates)):
            d=commit_dates[i].rstrip().replace("Date:   ","").split("+")[0] + "("+commit_comments[i][8:].rstrip()+")"
            commits[d]=commit_numbers[i][7:].rstrip()
            self.commitList.WholeList.append(d)
        self.commitList.listUpdate()
        self.fileList=SearchList("Files")
        self.fileList.list.currentItemChanged.connect(self.getHistory)
        self.layout.addWidget(self.commitList)
        self.layout.addWidget(self.fileList)
        
        self.mainLayout = QHBoxLayout()
        self.HistoryViewer = QTextBrowser()
        self.mainLayout.addLayout(self.layout)
        self.mainLayout.addWidget(self.HistoryViewer)
        self.mainLayout.setStretchFactor(self.layout,1)
        self.mainLayout.setStretchFactor(self.HistoryViewer,2)
        self.setLayout(self.mainLayout)
        
            
if __name__ == '__main__':
    if len(glob.glob(".git"))==0:
        print("Please execute in the directory has .git directory!")
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
