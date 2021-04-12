import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Elementos de Máquinas v1.0")
        self.setGeometry(150, 75, 1280, 720)
        self.setWindowIcon(QIcon("gears-icon-vector"))
        self.setStyleSheet("background-color: rgb(51, 51, 53)")
        #space for function calls
        self.MWSkeleton()
        self.MWSceneanView()
        

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


    def MWSceneanView (self):

        self.CenaMain = QGraphicsScene(self)

        self.pixmap1 = QGraphicsPixmapItem(QPixmap("gears-icon-vector"))
        self.pixmap1.setFlag(QGraphicsItem.ItemIsMovable)
        self.pixmap1.setScale(0.30)

        self.CenaMain.addItem(self.pixmap1)
        #logic test:
        def MWView (self):
            self.MainView = QGraphicsView(self.CenaMain, self)
            self.MainView.setGeometry(0, 45, 500, 675)
        MWView(self)


############################AnimationSection#################################




############################Ending###########################################
app = QApplication([])
janela = Window()
sys.exit(app.exec_())