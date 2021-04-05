import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore, QtQuick
from PyQt6.QtWidgets import QApplication, QWidget 
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()                                  #here we are extending the QWidget class, with the created class, wich makes everything easier
        self.setWindowTitle("Calculadora Elementos de Máquinas")  # setting the window title to machine elements calculator, an icon, and size/disposition on the screen 
        self.setWindowIcon(QIcon("gears-icon-vector.jpg"))
        self.setGeometry(150, 80, 1280, 720)
        self.setStyleSheet("background-color:gray")

app = QApplication([])                                      #Create a variable wich contains the QApplication built-in QWidgets
janela = Window()                                           #create a variable wich contains the window function built-in QWidgets
janela.show()                                               #now we show what we've created with the .function() thanks to object oriented programming

sys.exit(app.exec())                                        #instatiate the loop
