import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore, QtQuick
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("untitled6.qml")

view.setSource(url)
view.show()
app.exec_()

# Btn.clicked.connect(self.CreateWindow)cria o signal