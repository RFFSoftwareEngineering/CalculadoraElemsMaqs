import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore, QtQuick
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsTextItem
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Elementos de Máquinas")
        self.setWindowIcon(QIcon("gears-icon-vector.jpg"))
        self.setGeometry(150, 80, 1280, 720)
        self.setStyleSheet("background-color:gray")
        self.CreateButtons()
        self.CreateScene()
        
        
        
    def CreateButtons (self):
        Btn = QPushButton("Click Me", self)
        Btn.move(600, 310)
        Btn.setIcon(QIcon("gears-icon-vector.jpg"))
        Btn.clicked.connect(self.CreateWindow)#cria o signal

    def CreateScene (self):
        Cena = QGraphicsScene(self)#cria o scene      
        Cena.addText("hora de dormir")
        pix1 = QPixmap()
        pix1.load("gears-icon-vector.jpg")
        Cena.addPixmap(pix1.scaled(100, 100))#cria o pixmap a partir da imagem e diminui no caso
        Visao = QGraphicsView(Cena, self)#cria o view
        Visao.setGeometry(0, 0, 500, 720)
        Visao.show()

    def CreateLabels (self):#slot
        self.Label1 = QLabel("My Label", self)
        self.Label1.move(600, 210)
        self.Label1.setFont(QFont("Times New Roman", 15))
        self.Label1.show()
    def CreateWindow (self):
        self.Window2 = Window()#cria o slot
        self.setWindowTitle("janela 2 teste")
        self.setGeometry(120, 70, 600, 370)
        self.Window2.show()


app = QApplication([])
janela = Window()
janela.show()

sys.exit(app.exec())