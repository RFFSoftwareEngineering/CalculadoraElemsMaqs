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

        self.enginepic = QGraphicsPixmapItem(QPixmap("enginewallpaper"))
        self.enginepic.setFlag(QGraphicsItem.ItemIsMovable)
        self.enginepic.setScale(0.05)

        self.CenaMain.addItem(self.pixmap1)
        self.CenaMain.addItem(self.pixmap2)
        self.CenaMain.addItem(self.thehammer)
        self.CenaMain.addItem(self.sparkpix)
        self.CenaMain.addItem(self.planepix)
        self.CenaMain.addItem(self.shippix)
        self.CenaMain.addItem(self.gearpix)
        self.CenaMain.addItem(self.enginepic)

        #logic test:
        def MWView (self):
            self.MainView = QGraphicsView(self.CenaMain, self)
            self.MainView.setGeometry(0, 45, 500, 675)
        MWView(self)


############################AnimationSection(MainWindow)#################################


    def LinhaofTempo (self):
        #def timeline and timer

        self.linha = QTimeLine(20000)
        self.linha.setFrameRange(0, 20000)
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
            self.animenation.setRotationAt(0.001, -5)
            self.animenation.setRotationAt(0.0015, 0)
            self.animenation.setRotationAt(0.0022, -5)
            self.animenation.setRotationAt(0.0027, 0)
            self.animenation.setRotationAt(0.0035, -5)
            self.animenation.setRotationAt(0.0045, 0)
            self.animenation.setRotationAt(0.0052, -5)
            self.animenation.setRotationAt(0.0060, 0)
            self.animenation.setRotationAt(0.0075, -5)
            self.animenation.setRotationAt(0.0085, 0)
            self.animenation.setRotationAt(0.0092, -5)
            self.animenation.setRotationAt(0.01, 0)
            self.animenation.setPosAt(0.012, QPointF(150.0, 520.0))
            self.animenation.setPosAt(0.014, QPointF(150, 600.0))
            self.animenation.setPosAt(0.017, QPointF(150, 800))

        #animation2:
        
        def Ani2 (self):

            self.animation2 = QGraphicsItemAnimation(self)
            self.animation2.setTimeLine(self.linha)
            self.animation2.setItem(self.pixmap2)
            self.animation2.setPosAt(0.0, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0, -33.0)
            self.animation2.setPosAt(0.003, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.004, -3.0)
            self.animation2.setPosAt(0.004, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.0041, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.007, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.007, -33.0)
            self.animation2.setPosAt(0.008, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.008, -3.0)
            self.animation2.setPosAt(0.008, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.0081, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.0091, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0091, -33.0)
            self.animation2.setPosAt(0.0096, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.0097, -3.0)
            self.animation2.setPosAt(0.0098, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.010, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.012, QPointF(-140.0, 10.0))
            self.animation2.setPosAt(0.014, QPointF(-90, -80))
            self.animation2.setPosAt(0.017, QPointF(-90, -250))


        #animation3(the hammer):

        def HammerAni (self):

            self.hammerAnim = QGraphicsItemAnimation(self)
            self.hammerAnim.setTimeLine(self.linha)
            self.hammerAnim.setItem(self.thehammer)
            self.hammerAnim.setPosAt(0.0, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0, -160.0)
            self.hammerAnim.setRotationAt(0.0015, -100.0)
            self.hammerAnim.setPosAt(0.0016, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.003, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.003, -160.0)
            self.hammerAnim.setRotationAt(0.0035, -100.0)
            self.hammerAnim.setPosAt(0.0036, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.006, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.006, -160.0)
            self.hammerAnim.setRotationAt(0.0065, -100.0)
            self.hammerAnim.setPosAt(0.0066, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0090, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0090, -160.0)
            self.hammerAnim.setRotationAt(0.010, -100.0)
            self.hammerAnim.setPosAt(0.010, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.012, QPointF(360.0, 350.0))
            self.hammerAnim.setPosAt(0.014, QPointF(420.0, 380))
            self.hammerAnim.setPosAt(0.017, QPointF(580, 380))

        #animation4:

        def SparkAni (self):

            self.sparkanim = QGraphicsItemAnimation(self)
            self.sparkanim.setTimeLine(self.linha)
            self.sparkanim.setItem(self.sparkpix)
            self.sparkanim.setPosAt(0.0, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00155, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.0016, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.0017, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.00355, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.0036, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.0037, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.00655, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.0066, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.0067, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.00955, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.010, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.010, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.012, QPointF(410.0, 200.0))
            self.sparkanim.setPosAt(0.014, QPointF(500.0, 200))

        #animation5:

        def PlaneAni (self):

            self.planeanimation = QGraphicsItemAnimation(self)
            self.planeanimation.setTimeLine(self.linha)
            self.planeanimation.setItem(self.planepix)
            self.planeanimation.setPosAt(0.0, QPointF(40.0, 320.0))
            self.planeanimation.setRotationAt(0.0, 90.0)
            self.planeanimation.setPosAt(0.001, QPointF(150, 320))
            self.planeanimation.setPosAt(0.002, QPointF(260, 320))
            self.planeanimation.setPosAt(0.003, QPointF(450, 320))
            self.planeanimation.setPosAt(0.004, QPointF(690, 320))
            
        #animation6:

        def ShipAni (self):

            self.shipanimation = QGraphicsItemAnimation(self)
            self.shipanimation.setTimeLine(self.linha)
            self.shipanimation.setItem(self.shippix)
            self.shipanimation.setPosAt(0.0, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.004, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.005, QPointF(400, 320))
            self.shipanimation.setPosAt(0.0065, QPointF(300, 320))
            self.shipanimation.setPosAt(0.008, QPointF(180, 310))
            self.shipanimation.setPosAt(0.009, QPointF(40, 320))
            self.shipanimation.setPosAt(0.010, QPointF(-120, 320))
            self.shipanimation.setPosAt(0.012, QPointF(-160, 320))
            self.shipanimation.setPosAt(0.014, QPointF(-250, 320))

        #animation7:

        def GearAni (self):

            self.gearanimation1 = QGraphicsItemAnimation(self)
            self.gearanimation1.setTimeLine(self.linha)
            self.gearanimation1.setItem(self.gearpix)
            self.gearanimation1.setPosAt(0.0, QPointF(300.0, 20.0))
            self.gearanimation1.setRotationAt(0.01, 25)
            self.gearanimation1.setPosAt(0.0009, QPointF(315.0, 13.0))
            self.gearanimation1.setRotationAt(0.002, 50)
            self.gearanimation1.setPosAt(0.0019, QPointF(330.0, 10.0))
            self.gearanimation1.setRotationAt(0.003, 75)
            self.gearanimation1.setPosAt(0.0029, QPointF(345.0, 15.0))
            self.gearanimation1.setRotationAt(0.004, 90)
            self.gearanimation1.setPosAt(0.0039, QPointF(355.0, 20.0))
            self.gearanimation1.setRotationAt(0.005, 105)
            self.gearanimation1.setPosAt(0.0049, QPointF(360.0, 30.0))
            self.gearanimation1.setRotationAt(0.006, 145)
            self.gearanimation1.setPosAt(0.0059, QPointF(365.0, 55.0))
            self.gearanimation1.setRotationAt(0.007, 190)
            self.gearanimation1.setPosAt(0.0069, QPointF(340.0, 80.0))
            self.gearanimation1.setRotationAt(0.008, 240)
            self.gearanimation1.setPosAt(0.0079, QPointF(320.0, 82.0))
            self.gearanimation1.setRotationAt(0.010, 360)
            self.gearanimation1.setPosAt(0.0099, QPointF(305.0, 35.0))
            self.gearanimation1.setPosAt(0.012, QPointF(305.0, 10.0))
            self.gearanimation1.setPosAt(0.014, QPointF(305.0, -50))

        #animation8:

        def Pic1Ani (self):

            self.engineanim = QGraphicsItemAnimation(self)
            self.engineanim.setTimeLine(self.linha)
            self.engineanim.setItem(self.enginepic)
            self.engineanim.setPosAt(0.0, QPointF(0.0, 0.0))
            self.engineanim.setScaleAt(0.0, 0.1, 0.1)
            self.engineanim.setPosAt(0.012, QPointF(100, 100))
            self.engineanim.setPosAt(0.014, QPointF(200, 200))
            self.engineanim.setScaleAt(0.0139, 0.1, 0.1)
            self.engineanim.setScaleAt(0.016, 0.35, 0.35)
            self.engineanim.setPosAt(0.016, QPointF(260, 260))
            self.engineanim.setScaleAt(0.017, 0.55, 0.55)
            self.engineanim.setScaleAt(0.02, 1.2, 1.2)
            self.engineanim.setPosAt(0.021, QPointF(240, 240))
            self.engineanim.setScaleAt(0.044, 2.2, 2.2)
            self.engineanim.setPosAt(0.043, QPointF(180, 180))
            self.engineanim.setScaleAt(0.067, 4.4, 4.4)
            self.engineanim.setPosAt(0.067, QPointF(90, 130))
            self.engineanim.setPosAt(0.098, QPointF(40, 130))
            self.engineanim.setScaleAt(0.100, 6.2, 6.2)
            self.engineanim.setPosAt(0.120, QPointF(20, 80))
            self.engineanim.setScaleAt(0.140, 7.1, 7.1)
            self.engineanim.setPosAt(0.140, QPointF(0, 20))
            self.engineanim.setScaleAt(0.160, 8, 8)
            self.engineanim.setPosAt(0.160, QPointF(-30, 15))
            self.engineanim.setScaleAt(0.190, 1.2, 1.2)
            self.engineanim.setPosAt(0.190, QPointF(-80, -15))
            self.engineanim.setPosAt(0.220, QPointF(-220, -220))

        #animations finalization: 
           
        Anime(self)
        Ani2(self)
        HammerAni(self)
        SparkAni(self)
        PlaneAni(self)
        ShipAni(self)
        GearAni(self)
        Pic1Ani(self)
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
        #test:
        self.Butao = QPushButton("teste3", self.GearsWindow)
        self.Butao.move(160, 90)
        self.Butao.clicked.connect(self.WindowInWindow)

    def WindowInWindow (self):

        self.Windowisidewindow = QWidget()
        self.Windowisidewindow.show()

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