import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsItem
#clean restart
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Elementos de Máquinas")
        self.setGeometry(150, 100, 1280, 720)
        self.setWindowIcon(QIcon("gears-icon-vector"))
        #space for function calls

        self.show()
#space to def new functions, objective == clean and functional code
#clean restart
app = QApplication([])
janela = Window()
sys.exit(app.exec_())