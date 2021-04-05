import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore, QtQuick
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Elementos de Máquinas")
        self.setWindowIcon(QIcon("gears-icon-vector.jpg"))
        self.setGeometry(150, 80, 1280, 720)
        self.setStyleSheet("background-color:gray")
        self.CreateButtons()
        
        
        
    def CreateButtons (self):
        Btn = QPushButton("Click Me", self)
        Btn.move(600, 310)
        Btn.setIcon(QIcon("gears-icon-vector.jpg"))
        Btn.clicked.connect(self.CreateLabels)#cria o signal

    def CreateLabels (self):
        self.Label1 = QLabel("My Label", self)
        self.Label1.move(600, 210)
        self.Label1.setFont(QFont("Times New Roman", 15))
        self.Label1.show()
    

app = QApplication([])
janela = Window()
janela.show()

sys.exit(app.exec())