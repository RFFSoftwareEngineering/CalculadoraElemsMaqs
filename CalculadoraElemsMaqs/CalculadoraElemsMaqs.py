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
        self.CreateButton()
        self.show()

    
            
        


    #def CreateScene(self):

        #Cena = QGraphicsScene(self)

        
        #pixmap1 = QGraphicsPixmapItem(QPixmap("gears-icon-vector"))
        #pixmap1.setFlag(QGraphicsItem.ItemIsMovable)
        #pixmap1.setScale(0.25)
        

        #linha = QTimeLine(10000)
        #linha.setFrameRange(0, 1000)
        #linha.start()
        
        
        #timer = QTimer()
        #timer.isSingleShot()
        
       

        #animacao = QGraphicsItemAnimation(self)
        #animacao.setTimeLine(linha)
        #animacao.setItem(pixmap1)
        #animacao.setPosAt(0.0, QPointF(0.0, 0.0))
       
        

    
        


        
        #Cena.addItem(pixmap1)
    
        #self.Visao = QGraphicsView(Cena, self)
        #self.Visao.setGeometry(0, 0, 500, 720)
        #self.Visao.show()
         

    def CreateButton (self):
        Botao1 = QPushButton("click me test", self)
        Botao1.move(600, 220)
        Botao1.clicked.connect(self.SlotTest)
    

    def SlotTest (self):
        teste = QTransform()
        teste.rotate(4.0)
        pixmap1 = QGraphicsPixmapItem(QPixmap("gears-icon-vector"))
        pixmap1.setFlag(QGraphicsItem.ItemIsMovable)
        pixmap1.setScale(0.25)
        pixmap1.setTransform(teste)
        Cena = QGraphicsScene(self)
        Cena.addItem(pixmap1)
        self.Visao = QGraphicsView(Cena, self)
        self.Visao.setGeometry(0, 0, 500, 720)
        self.Visao.show()

    



app = QApplication([])
janela = Window()
sys.exit(app.exec_())