import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Elementos de Máquinas v1.0")
        self.setGeometry(150, 75, 1280, 720)
        self.setWindowIcon(QIcon("gear-icon-vector"))
        self.setStyleSheet("background-color: rgb(51, 51, 53)")
        #space for function calls
        self.MWSkeleton()
        self.MWSceneanView()
        self.LinhaofTempo()
        self.MainWindowBtns()
        self.show()


#########################################################################
#MainWindow:
    def MWSkeleton (self):

        self.LabelTtl = QLabel("Calculadora de Elementos de Máquinas", self)
        self.LabelTtl.setFont(QFont("Arial", 20, 8, True))
        self.LabelTtl.move(350, 10)
        self.LabelTtl.setStyleSheet("color: rgb(17, 11, 26)")
        self.LabelInfo1 = QLabel("Escolha o Elemento:", self)
        self.LabelInfo1.setFont(QFont("Arial", 16, 2, True))
        self.LabelInfo1.setStyleSheet("color: rgb(17, 11, 26)")
        self.LabelInfo1.move(800, 50)

#MainWindow Scene and View
    def MWSceneanView (self):

        self.CenaMain = QGraphicsScene(self)
        #pixmaps prep:
        self.pixmap1 = QGraphicsPixmapItem(QPixmap("engine"))
        self.pixmap1.setFlag(QGraphicsItem.ItemIsMovable)
        self.pixmap1.setScale(0.26)

        self.pixmap2 = QGraphicsPixmapItem(QPixmap("chave-parafuso"))
        self.pixmap2.setFlag(QGraphicsItem.ItemIsMovable)
        self.pixmap2.setScale(0.4)

        self.thehammer = QGraphicsPixmapItem(QPixmap("thor-hammer-icon"))
        self.thehammer.setFlag(QGraphicsItem.ItemIsMovable)
        self.thehammer.setScale(0.4)

        self.sparkpix = QGraphicsPixmapItem(QPixmap("sparky"))
        self.sparkpix.setScale(0.5)

        self.planepix = QGraphicsPixmapItem(QPixmap("plane"))
        self.planepix.setFlag(QGraphicsItem.ItemIsMovable)
        self.planepix.setScale(0.8)

        self.shippix = QGraphicsPixmapItem(QPixmap("cargoship"))
        self.shippix.setFlag(QGraphicsItem.ItemIsMovable)
        self.shippix.setScale(1.0)

        self.gearpix = QGraphicsPixmapItem(QPixmap("gear-icon-vector"))
        self.gearpix.setFlag(QGraphicsItem.ItemIsMovable)
        self.gearpix.setScale(0.1)

        self.CenaMain.addItem(self.pixmap1)
        self.CenaMain.addItem(self.pixmap2)
        self.CenaMain.addItem(self.thehammer)
        self.CenaMain.addItem(self.sparkpix)
        self.CenaMain.addItem(self.planepix)
        self.CenaMain.addItem(self.shippix)
        self.CenaMain.addItem(self.gearpix)

        #logic test:
        def MWView (self):
            self.MainView = QGraphicsView(self.CenaMain, self)
            self.MainView.setGeometry(0, 45, 500, 675)
        MWView(self)


############################AnimationSection(MainWindow)#################################


    def LinhaofTempo (self):
        #def timeline and timer

        self.linha = QTimeLine(2000)
        self.linha.setFrameRange(0, 1000)
        self.linha.setLoopCount(0)

        def reloginho (self):

            self.timer = QTimer()
            self.timer.isSingleShot()

        reloginho(self) #call timer

        #MainWindow anims, animation1:

        def Anime (self):

            self.animenation = QGraphicsItemAnimation(self)
            self.animenation.setTimeLine(self.linha)
            self.animenation.setItem(self.pixmap1)
            self.animenation.setPosAt(0.0, QPointF(150.0, 480.0))
            self.animenation.setRotationAt(0.1, -5)
            self.animenation.setRotationAt(0.15, 0)
            self.animenation.setRotationAt(0.22, -5)
            self.animenation.setRotationAt(0.27, 0)
            self.animenation.setRotationAt(0.35, -5)
            self.animenation.setRotationAt(0.45, 0)
            self.animenation.setRotationAt(0.52, -5)
            self.animenation.setRotationAt(0.60, 0)
            self.animenation.setRotationAt(0.75, -5)
            self.animenation.setRotationAt(0.85, 0)
            self.animenation.setRotationAt(0.92, -5)
            self.animenation.setRotationAt(1.0, 0)

        #animation2:
        
        def Ani2 (self):

            self.animation2 = QGraphicsItemAnimation(self)
            self.animation2.setTimeLine(self.linha)
            self.animation2.setItem(self.pixmap2)
            self.animation2.setPosAt(0.0, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0, -33.0)
            self.animation2.setPosAt(0.3, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.4, -3.0)
            self.animation2.setPosAt(0.4, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.41, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.7, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.7, -33.0)
            self.animation2.setPosAt(0.8, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.8, -3.0)
            self.animation2.setPosAt(0.8, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.81, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.91, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.91, -33.0)
            self.animation2.setPosAt(0.96, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.97, -3.0)
            self.animation2.setPosAt(0.98, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(1.0, QPointF(-180.0, 50.0))


        #animation3(the hammer):

        def HammerAni (self):

            self.hammerAnim = QGraphicsItemAnimation(self)
            self.hammerAnim.setTimeLine(self.linha)
            self.hammerAnim.setItem(self.thehammer)
            self.hammerAnim.setPosAt(0.0, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0, -160.0)
            self.hammerAnim.setRotationAt(0.15, -100.0)
            self.hammerAnim.setPosAt(0.16, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.3, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.3, -160.0)
            self.hammerAnim.setRotationAt(0.35, -100.0)
            self.hammerAnim.setPosAt(0.36, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.6, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.6, -160.0)
            self.hammerAnim.setRotationAt(0.65, -100.0)
            self.hammerAnim.setPosAt(0.66, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.90, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.90, -160.0)
            self.hammerAnim.setRotationAt(1.0, -100.0)
            self.hammerAnim.setPosAt(1.0, QPointF(320.0, 350.0))

        #animation4:

        def SparkAni (self):

            self.sparkanim = QGraphicsItemAnimation(self)
            self.sparkanim.setTimeLine(self.linha)
            self.sparkanim.setItem(self.sparkpix)
            self.sparkanim.setPosAt(0.0, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.155, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.16, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.17, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.355, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.36, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.37, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.655, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.66, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.67, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.955, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(1.0, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(1.0, QPointF(385.0, 200.0))

        #animation5:

        def PlaneAni (self):

            self.planeanimation = QGraphicsItemAnimation(self)
            self.planeanimation.setTimeLine(self.linha)
            self.planeanimation.setItem(self.planepix)
            self.planeanimation.setPosAt(0.0, QPointF(40.0, 320.0))
            self.planeanimation.setRotationAt(0.0, 90.0)
            self.planeanimation.setPosAt(0.1, QPointF(150, 320))
            self.planeanimation.setPosAt(0.2, QPointF(260, 320))
            self.planeanimation.setPosAt(0.3, QPointF(450, 320))
            self.planeanimation.setPosAt(0.4, QPointF(690, 320))
            
        #animation6:

        def ShipAni (self):

            self.shipanimation = QGraphicsItemAnimation(self)
            self.shipanimation.setTimeLine(self.linha)
            self.shipanimation.setItem(self.shippix)
            self.shipanimation.setPosAt(0.0, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.4, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.5, QPointF(400, 320))
            self.shipanimation.setPosAt(0.65, QPointF(300, 320))
            self.shipanimation.setPosAt(0.8, QPointF(180, 310))
            self.shipanimation.setPosAt(0.9, QPointF(40, 320))
            self.shipanimation.setPosAt(1.0, QPointF(-120, 320))

        #animation7:

        def GearAni (self):

            self.gearanimation1 = QGraphicsItemAnimation(self)
            self.gearanimation1.setTimeLine(self.linha)
            self.gearanimation1.setItem(self.gearpix)
            self.gearanimation1.setPosAt(0.0, QPointF(300.0, 20.0))
            self.gearanimation1.setRotationAt(0.1, 25)
            self.gearanimation1.setPosAt(0.09, QPointF(315.0, 13.0))
            self.gearanimation1.setRotationAt(0.2, 50)
            self.gearanimation1.setPosAt(0.19, QPointF(330.0, 10.0))
            self.gearanimation1.setRotationAt(0.3, 75)
            self.gearanimation1.setPosAt(0.29, QPointF(345.0, 15.0))
            self.gearanimation1.setRotationAt(0.4, 90)
            self.gearanimation1.setPosAt(0.39, QPointF(355.0, 20.0))
            self.gearanimation1.setRotationAt(0.5, 105)
            self.gearanimation1.setPosAt(0.49, QPointF(360.0, 30.0))
            self.gearanimation1.setRotationAt(0.6, 145)
            self.gearanimation1.setPosAt(0.59, QPointF(365.0, 55.0))
            self.gearanimation1.setRotationAt(0.7, 190)
            self.gearanimation1.setPosAt(0.69, QPointF(340.0, 80.0))
            self.gearanimation1.setRotationAt(0.8, 240)
            self.gearanimation1.setPosAt(0.79, QPointF(320.0, 82.0))
            self.gearanimation1.setRotationAt(1.0, 360)
            self.gearanimation1.setPosAt(0.99, QPointF(305.0, 35.0))

        #animations finalization: 
           
        Anime(self)
        Ani2(self)
        HammerAni(self)
        SparkAni(self)
        PlaneAni(self)
        ShipAni(self)
        GearAni(self)
        #TimelineCall:
        self.linha.start()

#############################################################################
#Main-Window Buttons:

    def MainWindowBtns (self):

        self.TesteBtn = QPushButton("test", self)
        self.TesteBtn.move(800, 200)
        self.TesteBtn.clicked.connect(self.CreateNewWin)
#gears Window:

    def CreateNewWin (self):
        self.GearsWindow = QWidget()
        self.GearsWindow.setGeometry(650, 190, 780, 602)
        self.GearsWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.GearsWindow.setWindowTitle("Seção das Engrenagens")
        #space for function calls:
        self.MWSk()
        self.SomaFields()
        self.GearsWindow.show()
#gears window functions:

    def MWSk (self):

        self.LabelT = QLabel("Calculadora de Elementos de Máquinas", self.GearsWindow)

#test:

    def SomaFields (self):

        self.field1 = QLineEdit("teste", self.GearsWindow)
        self.field1.move(0, 20)
        self.field2 = QLineEdit("teste2", self.GearsWindow)
        self.field2.move(150, 20)
        self.Calcular = QPushButton("soma", self.GearsWindow)
        self.Calcular.move(100, 50)
        self.Calcular.clicked.connect(self.TesteSoma)

    def TesteSoma (self):

        self.Input1 = self.field1.text()
        self.Input2 = self.field2.text()
        self.a = float(self.Input1)
        self.b = float(self.Input2)
        self.res = self.a + self.b
        self.ResultadoField = QLabel("teste" , self.GearsWindow)
        self.ResultadoField.setText(str(self.res))
        self.ResultadoField.move(75, 80)
        self.ResultadoField.show()
        
        
        

        
        
 
############################Ending###########################################

if __name__ == "__main__":
    app = QApplication([])
    janela = MainWindow()
    sys.exit(app.exec_())