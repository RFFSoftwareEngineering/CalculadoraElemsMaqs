import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsItem

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Elementos de Máquinas")
        self.setGeometry(150, 100, 1280, 720)
        self.setWindowIcon(QIcon("gears-icon-vector"))
        self.show()
        self.CreateScene()


    def CreateScene(self):

        Cena = QGraphicsScene(self)
        texto = Cena.addText("teste")

        pixmap1 = QGraphicsPixmapItem(QPixmap("gears-icon-vector"))
        pixmap1.setFlag(QGraphicsItem.ItemIsMovable)
        pixmap1.setScale(0.4)

        item = QtWidgets.QGraphicsRectItem(0, 0, 200, 200)
        texto.setFlag(QGraphicsItem.ItemIsMovable)
        item.setFlag(QGraphicsItem.ItemIsMovable)
        

        Cena.addItem(item)
        Cena.addItem(pixmap1)

        self.Visao = QGraphicsView(Cena, self)
        self.Visao.setGeometry(0, 0, 500, 720)
        self.Visao.show()


app = QApplication([])
janela = Window()
sys.exit(app.exec_())