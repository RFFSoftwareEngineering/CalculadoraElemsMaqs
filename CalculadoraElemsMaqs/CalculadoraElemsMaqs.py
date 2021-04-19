import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Elementos de Máquinas v1.0")
        self.setGeometry(150, 75, 1280, 720)
        self.setWindowIcon(QIcon("gear-icon-vector"))
        self.setStyleSheet("background-color: rgb(51, 51, 53)")
        #space for function calls in the main window
        self.MWSkeleton()
        self.MainWindowBtns()
        self.show()


#########################################################################
    def MWSkeleton (self):

        self.LabelTtl = QLabel("Calculadora de Elementos de Máquinas", self)
        self.LabelTtl.setFont(QFont("Arial", 20, 8, True))
        self.LabelTtl.move(350, 10)
        self.LabelTtl.setStyleSheet("color: rgb(17, 11, 26)")
        self.LabelInfo1 = QLabel("Escolha o Elemento:", self)
        self.LabelInfo1.setFont(QFont("Arial", 16, 2, True))
        self.LabelInfo1.setStyleSheet("color: rgb(17, 11, 26)")
        self.LabelInfo1.move(800, 50)


#############################################################################

#functional part(test):
    
#Main-Window Buttons:

    def MainWindowBtns (self):

        self.TesteBtn = QPushButton("test", self)
        self.TesteBtn.move(800, 200)
        self.TesteBtn.clicked.connect(self.CreateNewWin)

    def CreateNewWin (self):
        self.TestWindow = QWidget()
        self.TestWindow.setGeometry(200, 200, 400, 400)
        self.MWSk()
        self.TestWindow.show()

    def MWSk (self):

        self.LabelT = QLabel("Calculadora de Elementos de Máquinas", self.TestWindow)
        self.LabelT.show()





############################Ending###########################################
if __name__ == "__main__":
    app = QApplication([])
    janela = MainWindow()
    sys.exit(app.exec_())