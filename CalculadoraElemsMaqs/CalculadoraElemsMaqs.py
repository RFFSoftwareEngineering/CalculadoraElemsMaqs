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
        self.LinhaofTempo()

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
        self.pixmap1.toGraphicsObject()

        self.CenaMain.addItem(self.pixmap1)
        #logic test:
        def MWView (self):
            self.MainView = QGraphicsView(self.CenaMain, self)
            self.MainView.setGeometry(0, 45, 500, 675)
        MWView(self)


############################AnimationSection#################################


    def LinhaofTempo (self):

        self.linha = QTimeLine(1000)
        self.linha.setFrameRange(0, 1000)
        self.linha.setLoopCount(0)
        def reloginho (self):
            self.timer = QTimer()
            self.timer.isSingleShot()
        reloginho(self)
        def Anime (self):
            self.animenation = QGraphicsItemAnimation(self)
            self.animenation.setTimeLine(self.linha)
            self.animenation.setItem(self.pixmap1)
            self.animenation.setPosAt(0.0, QPointF(0.0, 0.0))
            self.animenation.setRotationAt(0.1, 30)
            
        Anime(self)
        self.linha.start()
        


############################Ending###########################################
app = QApplication([])
janela = Window()
sys.exit(app.exec_())