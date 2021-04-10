import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsItem

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teste")
        self.setGeometry(300, 200, 500, 500)
        self.show()
        self.CreateUI()
        
        

    def CreateUI(self):
        
        scene = QGraphicsScene(self)
        texto = scene.addText("teste")
        item = QtWidgets.QGraphicsRectItem(0, 0, 200, 200)
        texto.setFlag(QGraphicsItem.ItemIsMovable)
        item.setFlag(QGraphicsItem.ItemIsMovable)
               
        scene.addItem(item)
        
   
        
        
            
        
        

        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(0, 0, 500, 500)
        self.view.show()


app = QApplication([])
window = Window()
sys.exit(app.exec_())