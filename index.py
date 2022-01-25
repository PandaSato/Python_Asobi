from MPL import *

def XButton(buttonName, function):
    button = QPushButton(buttonName)
    button.clicked.connect(function)
    return button

def XVLayout(*components):
    layout = QVBoxLayout()
    for component in components:
        try:
            layout.addWidget(component)
        except:
            layout.addLayout(component)
    return layout

def XHLayout(*components):
    layout = QHBoxLayout()
    for component in components:
        try:
            layout.addWidget(component)
        except:
            layout.addLayout(component)
    return layout


##dummy function
def dummy():
    print("dummy")
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(800,400)
        self.setLayout(XVLayout(XButton("New Project",dummy)))
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    mwindow.show()
    app.exec_()
