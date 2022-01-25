from MPL import *


def XTableView(*headerLabels):
    table = QTableWidget()
    table.setColumnCount(len(headerLabels))
    table.setHorizontalHeaderLabels(headerLabels)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
    #table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) 
    #table.horizontalHeader().setSectionResizeMode(len(headerLabels)-1, QHeaderView.Stretch) # Stretch Last header
    return table
##dummy function
def dummy():
    print("dummy")
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,400)
        #self.setLayout(XVLayout(XButton("Test",dummy),XButton("Hello World",dummy),XHLayout(XButton('a',dummy),XButton('b',dummy))))
        self.setLayout(XVLayout(XTableView('Part 1','Part 2','Part 3'),XHLayout(XButton('Save Data',dummy),XButton('Add Data',dummy),1)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
