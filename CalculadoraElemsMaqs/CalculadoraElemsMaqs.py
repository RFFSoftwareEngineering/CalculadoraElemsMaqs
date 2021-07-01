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
        self.LabelInfo1.move(800, 70)

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

        self.trainpix = QGraphicsPixmapItem(QPixmap("trainpic"))
        self.trainpix.setFlag(QGraphicsItem.ItemIsMovable)
        self.trainpix.setScale(0.2)

        self.furnacepix = QGraphicsPixmapItem(QPixmap("furnace"))
        self.furnacepix.setFlag(QGraphicsItem.ItemIsMovable)
        self.furnacepix.setScale(0.7)

        self.naviopix = QGraphicsPixmapItem(QPixmap("cargoshippic"))
        self.naviopix.setFlag(QGraphicsItem.ItemIsMovable)
        self.naviopix.setScale(0.4)

        self.aviaopix = QGraphicsPixmapItem(QPixmap("planepic"))
        self.aviaopix.setFlag(QGraphicsItem.ItemIsMovable)
        self.aviaopix.setScale(0.12)

        self.Titulopix = QGraphicsPixmapItem(QPixmap("tituloELM"))
        self.Titulopix.setFlag(QGraphicsItem.ItemIsMovable)
        self.Titulopix.setScale(0.1)


        self.CenaMain.addItem(self.pixmap1)
        self.CenaMain.addItem(self.pixmap2)
        self.CenaMain.addItem(self.thehammer)
        self.CenaMain.addItem(self.sparkpix)
        self.CenaMain.addItem(self.planepix)
        self.CenaMain.addItem(self.shippix)
        self.CenaMain.addItem(self.gearpix)
        self.CenaMain.addItem(self.enginepic)
        self.CenaMain.addItem(self.trainpix)
        self.CenaMain.addItem(self.furnacepix)
        self.CenaMain.addItem(self.naviopix)
        self.CenaMain.addItem(self.aviaopix)
        self.CenaMain.addItem(self.Titulopix)

        #logic test:
        def MWView (self):
            self.MainView = QGraphicsView(self.CenaMain, self)
            self.MainView.setGeometry(0, 45, 500, 675)
        MWView(self)


############################AnimationSection(MainWindow)#################################


    def LinhaofTempo (self):
        #def timeline and timer

        self.linha = QTimeLine(70000)
        self.linha.setFrameRange(0, 20000)
        self.linha.setLoopCount(3)

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
            self.animenation.setRotationAt(0.0001, -5)
            self.animenation.setRotationAt(0.00015, 0)
            self.animenation.setRotationAt(0.00022, -5)
            self.animenation.setRotationAt(0.00027, 0)
            self.animenation.setRotationAt(0.00035, -5)
            self.animenation.setRotationAt(0.00045, 0)
            self.animenation.setRotationAt(0.00052, -5)
            self.animenation.setRotationAt(0.00060, 0)
            self.animenation.setRotationAt(0.00075, -5)
            self.animenation.setRotationAt(0.00085, 0)
            self.animenation.setRotationAt(0.00092, -5)
            self.animenation.setRotationAt(0.001, 0)
            self.animenation.setPosAt(0.0012, QPointF(150.0, 520.0))
            self.animenation.setPosAt(0.0014, QPointF(150, 600.0))
            self.animenation.setPosAt(0.0017, QPointF(150, 800))

        #animation2:
        
        def Ani2 (self):

            self.animation2 = QGraphicsItemAnimation(self)
            self.animation2.setTimeLine(self.linha)
            self.animation2.setItem(self.pixmap2)
            self.animation2.setPosAt(0.0, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0, -33.0)
            self.animation2.setPosAt(0.0003, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.0004, -3.0)
            self.animation2.setPosAt(0.0004, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.00041, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.0007, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0007, -33.0)
            self.animation2.setPosAt(0.0008, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.0008, -3.0)
            self.animation2.setPosAt(0.0008, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.00081, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.00091, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.00091, -33.0)
            self.animation2.setPosAt(0.00096, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.00097, -3.0)
            self.animation2.setPosAt(0.00098, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.0010, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.0012, QPointF(-140.0, 10.0))
            self.animation2.setPosAt(0.0014, QPointF(-90, -80))
            self.animation2.setPosAt(0.0017, QPointF(-90, -250))


        #animation3(the hammer):

        def HammerAni (self):

            self.hammerAnim = QGraphicsItemAnimation(self)
            self.hammerAnim.setTimeLine(self.linha)
            self.hammerAnim.setItem(self.thehammer)
            self.hammerAnim.setPosAt(0.0, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0, -160.0)
            self.hammerAnim.setRotationAt(0.00015, -100.0)
            self.hammerAnim.setPosAt(0.00016, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0003, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0003, -160.0)
            self.hammerAnim.setRotationAt(0.00035, -100.0)
            self.hammerAnim.setPosAt(0.00036, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0006, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0006, -160.0)
            self.hammerAnim.setRotationAt(0.00065, -100.0)
            self.hammerAnim.setPosAt(0.00066, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.00090, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.00090, -160.0)
            self.hammerAnim.setRotationAt(0.0010, -100.0)
            self.hammerAnim.setPosAt(0.0010, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0012, QPointF(360.0, 350.0))
            self.hammerAnim.setPosAt(0.0014, QPointF(420.0, 380))
            self.hammerAnim.setPosAt(0.0017, QPointF(580, 380))

        #animation4:

        def SparkAni (self):

            self.sparkanim = QGraphicsItemAnimation(self)
            self.sparkanim.setTimeLine(self.linha)
            self.sparkanim.setItem(self.sparkpix)
            self.sparkanim.setPosAt(0.0, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.000155, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00016, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.00017, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.000355, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00036, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.00037, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.000655, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00066, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.00067, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.000955, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.0010, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.0010, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.0012, QPointF(410.0, 200.0))
            self.sparkanim.setPosAt(0.0014, QPointF(500.0, 200))

        #animation5:

        def PlaneAni (self):

            self.planeanimation = QGraphicsItemAnimation(self)
            self.planeanimation.setTimeLine(self.linha)
            self.planeanimation.setItem(self.planepix)
            self.planeanimation.setPosAt(0.0, QPointF(40.0, 320.0))
            self.planeanimation.setRotationAt(0.0, 90.0)
            self.planeanimation.setPosAt(0.0001, QPointF(150, 320))
            self.planeanimation.setPosAt(0.0002, QPointF(260, 320))
            self.planeanimation.setPosAt(0.0003, QPointF(450, 320))
            self.planeanimation.setPosAt(0.0004, QPointF(690, 320))
            
        #animation6:

        def ShipAni (self):

            self.shipanimation = QGraphicsItemAnimation(self)
            self.shipanimation.setTimeLine(self.linha)
            self.shipanimation.setItem(self.shippix)
            self.shipanimation.setPosAt(0.0, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.0004, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.0005, QPointF(400, 320))
            self.shipanimation.setPosAt(0.00065, QPointF(300, 320))
            self.shipanimation.setPosAt(0.0008, QPointF(180, 310))
            self.shipanimation.setPosAt(0.0009, QPointF(40, 320))
            self.shipanimation.setPosAt(0.0010, QPointF(-120, 320))
            self.shipanimation.setPosAt(0.0012, QPointF(-160, 320))
            self.shipanimation.setPosAt(0.0014, QPointF(-250, 320))

        #animation7:

        def GearAni (self):

            self.gearanimation1 = QGraphicsItemAnimation(self)
            self.gearanimation1.setTimeLine(self.linha)
            self.gearanimation1.setItem(self.gearpix)
            self.gearanimation1.setPosAt(0.0, QPointF(300.0, 20.0))
            self.gearanimation1.setRotationAt(0.001, 25)
            self.gearanimation1.setPosAt(0.00009, QPointF(315.0, 13.0))
            self.gearanimation1.setRotationAt(0.0002, 50)
            self.gearanimation1.setPosAt(0.00019, QPointF(330.0, 10.0))
            self.gearanimation1.setRotationAt(0.0003, 75)
            self.gearanimation1.setPosAt(0.00029, QPointF(345.0, 15.0))
            self.gearanimation1.setRotationAt(0.0004, 90)
            self.gearanimation1.setPosAt(0.00039, QPointF(355.0, 20.0))
            self.gearanimation1.setRotationAt(0.0005, 105)
            self.gearanimation1.setPosAt(0.00049, QPointF(360.0, 30.0))
            self.gearanimation1.setRotationAt(0.0006, 145)
            self.gearanimation1.setPosAt(0.00059, QPointF(365.0, 55.0))
            self.gearanimation1.setRotationAt(0.0007, 190)
            self.gearanimation1.setPosAt(0.00069, QPointF(340.0, 80.0))
            self.gearanimation1.setRotationAt(0.0008, 240)
            self.gearanimation1.setPosAt(0.00079, QPointF(320.0, 82.0))
            self.gearanimation1.setRotationAt(0.0010, 360)
            self.gearanimation1.setPosAt(0.00099, QPointF(305.0, 35.0))
            self.gearanimation1.setPosAt(0.0012, QPointF(305.0, 10.0))
            self.gearanimation1.setPosAt(0.0014, QPointF(305.0, -50))

        #animation8:

        def Pic1Ani (self):

            self.engineanim = QGraphicsItemAnimation(self)
            self.engineanim.setTimeLine(self.linha)
            self.engineanim.setItem(self.enginepic)
            self.engineanim.setPosAt(0.0, QPointF(0.0, 0.0))
            self.engineanim.setScaleAt(0.0, 0.1, 0.1)
            self.engineanim.setPosAt(0.0012, QPointF(100, 100))
            self.engineanim.setPosAt(0.00125, QPointF(200, 200))
            self.engineanim.setScaleAt(0.00129, 0.1, 0.1)
            self.engineanim.setScaleAt(0.0014, 0.35, 0.35)
            self.engineanim.setPosAt(0.0014, QPointF(260, 260))
            self.engineanim.setScaleAt(0.0017, 0.55, 0.55)
            self.engineanim.setScaleAt(0.0019, 1.2, 1.2)
            self.engineanim.setPosAt(0.0021, QPointF(240, 240))
            self.engineanim.setScaleAt(0.0034, 2.2, 2.2)
            self.engineanim.setPosAt(0.0033, QPointF(180, 180))
            self.engineanim.setScaleAt(0.0047, 4.4, 4.4)
            self.engineanim.setPosAt(0.0047, QPointF(90, 130))
            self.engineanim.setPosAt(0.0048, QPointF(40, 130))
            self.engineanim.setScaleAt(0.0048, 6.2, 6.2)
            self.engineanim.setPosAt(0.00520, QPointF(20, 80))
            self.engineanim.setScaleAt(0.0540, 7.1, 7.1)
            self.engineanim.setPosAt(0.0140, QPointF(0, 20))
            self.engineanim.setScaleAt(0.0160, 8, 8)
            self.engineanim.setPosAt(0.0160, QPointF(-30, 15))
            self.engineanim.setScaleAt(0.0190, 8, 8)
            self.engineanim.setPosAt(0.0190, QPointF(-30, 15))
            self.engineanim.setScaleAt(0.0210, 8, 8)
            self.engineanim.setPosAt(0.0210, QPointF(-30, 15))
            self.engineanim.setPosAt(0.0225, QPointF(-888, -888))
            self.engineanim.setPosAt(0.77, QPointF(-888, -888))
            self.engineanim.setPosAt(0.79, QPointF(-38, 22))

        #animation9

        def Trainn (self):

            self.trainanim = QGraphicsItemAnimation(self)
            self.trainanim.setTimeLine(self.linha)
            self.trainanim.setItem(self.trainpix)
            self.trainanim.setPosAt(0.0, QPointF(600, 0))
            self.trainanim.setPosAt(0.0225, QPointF(600, 0))
            self.trainanim.setPosAt(0.0232, QPointF(100, 200))
            self.trainanim.setScaleAt(0.0238, 1.4, 1.4)
            self.trainanim.setPosAt(0.025, QPointF(30, 150))
            self.trainanim.setScaleAt(0.025, 1.9, 1.9)
            self.trainanim.setScaleAt(0.04, 3.1, 3.1)
            self.trainanim.setPosAt(0.04, QPointF(-150, -50))
            self.trainanim.setScaleAt(0.048, 4, 4)
            self.trainanim.setPosAt(0.048, QPointF(-290, -160))
            self.trainanim.setPosAt(0.052, QPointF(-320, -200))
            self.trainanim.setPosAt(0.07, QPointF(-500, -200))
            self.trainanim.setPosAt(0.088, QPointF(-770, -200))
            self.trainanim.setPosAt(0.095, QPointF(-1500, -600))

        #animation10:

        def FurnAn (self):

            self.fornonimation = QGraphicsItemAnimation(self)
            self.fornonimation.setTimeLine(self.linha)
            self.fornonimation.setItem(self.furnacepix)
            self.fornonimation.setPosAt(0.0, QPointF(-800, -600))
            self.fornonimation.setPosAt(0.095, QPointF(-800, -600))
            self.fornonimation.setPosAt(0.1, QPointF(100.0, 100.0))
            self.fornonimation.setScaleAt(0.1, 1.4, 1.4)
            self.fornonimation.setPosAt(0.125, QPointF(30, 130))
            self.fornonimation.setScaleAt(0.125, 1.9, 1.9)
            self.fornonimation.setPosAt(0.150, QPointF(-90, -20))
            self.fornonimation.setScaleAt(0.150, 2.3, 2.3)
            self.fornonimation.setPosAt(0.170, QPointF(-90, -20))
            self.fornonimation.setScaleAt(0.170, 2.3, 2.3)
            self.fornonimation.setPosAt(0.175, QPointF(-600, -20))
            self.fornonimation.setPosAt(0.180, QPointF(-980, -20))

        #animation11:

        def NavioAni (self):

            self.navionimation = QGraphicsItemAnimation(self)
            self.navionimation.setTimeLine(self.linha)
            self.navionimation.setItem(self.naviopix)
            self.navionimation.setPosAt(0.0, QPointF(-800, -600))
            self.navionimation.setPosAt(0.180, QPointF(-800, -600))
            self.navionimation.setPosAt(0.185, QPointF(-20.0, -20.0))
            self.navionimation.setScaleAt(0.186, 1.4, 1.4)
            self.navionimation.setPosAt(0.2, QPointF(20, 20))
            self.navionimation.setScaleAt(0.2, 1.9, 1.9)
            self.navionimation.setPosAt(0.225, QPointF(-20, 20))
            self.navionimation.setPosAt(0.250, QPointF(-50, 20))
            self.navionimation.setPosAt(0.275, QPointF(-80, 20))
            self.navionimation.setPosAt(0.3, QPointF(-110, 20))
            self.navionimation.setPosAt(0.325, QPointF(-140, 20))
            self.navionimation.setPosAt(0.350, QPointF(-170, 20))
            self.navionimation.setPosAt(0.375, QPointF(-200, 20))
            self.navionimation.setPosAt(0.400, QPointF(-230, 20))
            self.navionimation.setPosAt(0.410, QPointF(-1200, 20))

        #animation12:

        def AviaoAni (self):

            self.aviaoani = QGraphicsItemAnimation(self)
            self.aviaoani.setTimeLine(self.linha)
            self.aviaoani.setItem(self.aviaopix)
            self.aviaoani.setPosAt(0.0, QPointF(-800, -500))
            self.aviaoani.setPosAt(0.410, QPointF(-800, -500))
            self.aviaoani.setPosAt(0.415, QPointF(0, 0))
            self.aviaoani.setScaleAt(0.445, 1.8, 1.8)
            self.aviaoani.setPosAt(0.485, QPointF(-200, 0))
            self.aviaoani.setScaleAt(0.485, 2.4, 2.4)
            self.aviaoani.setPosAt(0.5, QPointF(-300, 20))
            self.aviaoani.setScaleAt(0.530, 2.0, 2.0)
            self.aviaoani.setPosAt(0.560, QPointF(0, 20))
            self.aviaoani.setPosAt(0.570, QPointF(-1200, 20))

        #animation12:

        def TituloAni (self):

            self.tituloani = QGraphicsItemAnimation(self)
            self.tituloani.setTimeLine(self.linha)
            self.tituloani.setItem(self.Titulopix)
            self.tituloani.setPosAt(0.0, QPointF(800, 0))
            self.tituloani.setPosAt(0.570, QPointF(800, 0))
            self.tituloani.setScaleAt(0.575, 9, 9)
            self.tituloani.setPosAt(0.576, QPointF(650, 0))
            self.tituloani.setPosAt(0.77, QPointF(-1100, 0))
            self.tituloani.setPosAt(0.85, QPointF(-2000, 0))

        #animations finalization: 
           
        Anime(self)
        Ani2(self)
        HammerAni(self)
        SparkAni(self)
        PlaneAni(self)
        ShipAni(self)
        GearAni(self)
        Pic1Ani(self)
        Trainn(self)
        FurnAn(self)
        NavioAni(self)
        AviaoAni(self)
        TituloAni(self)
        #TimelineCall:
        self.linha.start()

#############################################################################
#Main-Window Buttons:

    def MainWindowBtns (self):

        self.GearsBtn = QPushButton("Cálculo de Engrenagens", self)
        self.GearsBtn.setFont(QFont("Arial", 20, 8, True))
        self.GearsBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.GearsBtn.setIcon(QIcon("gear-icon-vector"))  
        self.GearsBtn.setIconSize(QSize(40, 40))
        self.GearsBtn.move(515, 140)
        self.GearsBtn.clicked.connect(self.CreateNewWin)

        self.ParafBtn = QPushButton("Cálculo de Paraf./Reb.", self)
        self.ParafBtn.setFont(QFont("Arial", 20, 8, True))
        self.ParafBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.ParafBtn.setIcon(QIcon("ParafusoIcon"))
        self.ParafBtn.setIconSize(QSize(40, 40))
        self.ParafBtn.move(915, 140)
        self.ParafBtn.clicked.connect(self.CreateScrewWindow)

        self.RoscaBtn = QPushButton("Cálculo de Roscas", self)
        self.RoscaBtn.setFont(QFont("Arial", 20, 8, True))
        self.RoscaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.RoscaBtn.setIcon(QIcon("roscaIcon"))
        self.RoscaBtn.setIconSize(QSize(40, 40))
        self.RoscaBtn.move(525, 240)
        self.RoscaBtn.clicked.connect(self.CreateRosca)

        self.MolasBtn = QPushButton("Cálculo de Molas", self)
        self.MolasBtn.setFont(QFont("Arial", 20, 8, True))
        self.MolasBtn.setStyleSheet("color: rgb(17 ,11, 26)")
        self.MolasBtn.setIcon(QIcon("MolaIcon"))
        self.MolasBtn.setIconSize(QSize(55, 55))
        self.MolasBtn.move(915, 240)
        self.MolasBtn.clicked.connect(self.CreateMolaW)

        self.EixoBtn = QPushButton("Cálculo de Eixos", self)
        self.EixoBtn.setFont(QFont("Arial", 20, 8, True))
        self.EixoBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.EixoBtn.setIcon(QIcon("eixoIcon"))
        self.EixoBtn.setIconSize(QSize(50, 50))
        self.EixoBtn.move(520, 340)
        self.EixoBtn.clicked.connect(self.CreateEixo)

        self.SoldaBtn = QPushButton("Cálculo de Solda", self)
        self.SoldaBtn.setFont(QFont("Arial", 20, 8, True))
        self.SoldaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.SoldaBtn.setIcon(QIcon("SoldaIcon"))
        self.SoldaBtn.setIconSize(QSize(61, 61))
        self.SoldaBtn.move(915, 340)
        self.SoldaBtn.clicked.connect(self.CreateSolda)

        self.PorcasBtn = QPushButton("Cálculo de Porcas", self)
        self.PorcasBtn.setFont(QFont("Arial", 20, 8, True))
        self.PorcasBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.PorcasBtn.setIcon(QIcon("PorcasIcon"))
        self.PorcasBtn.setIconSize(QSize(40, 40))
        self.PorcasBtn.move(520, 440)
        self.PorcasBtn.clicked.connect(self.CreatePorcas)

        self.MancaisBtn = QPushButton("Cálculo de Mancais", self)
        self.MancaisBtn.setFont(QFont("Arial", 20, 8, True))
        self.MancaisBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.MancaisBtn.setIcon(QIcon("mancalIcon"))
        self.MancaisBtn.setIconSize(QSize(61, 61))
        self.MancaisBtn.move(915, 440)
        self.MancaisBtn.clicked.connect(self.CreateMancais)

        self.CaboBtn = QPushButton("Cálculo de Cabos de Aço", self)
        self.CaboBtn.setFont(QFont("Arial", 20, 8, True))
        self.CaboBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.CaboBtn.setIcon(QIcon("CaboAlma"))
        self.CaboBtn.setIconSize(QSize(50, 50))
        self.CaboBtn.move(515, 540)
        self.CaboBtn.clicked.connect(self.CreateCabo)

        self.ChaveBtn = QPushButton("Cálculo de Chavetas", self)
        self.ChaveBtn.setFont(QFont("Arial", 20, 8, True))
        self.ChaveBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.ChaveBtn.setIcon(QIcon("chavetaIcon"))
        self.ChaveBtn.setIconSize(QSize(55, 55))
        self.ChaveBtn.move(920, 540)
        self.ChaveBtn.clicked.connect(self.CreateChave)
        
        

#gears Window:

    def CreateNewWin (self):
        self.GearsWindow = QWidget()
        self.GearsWindow.setGeometry(150, 150, 1280, 650)
        self.GearsWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.GearsWindow.setWindowTitle("Seção das Engrenagens")
        self.GearsWindow.setWindowIcon(QIcon("gear-icon-vector"))
        #space for function calls:
        self.MWSk()
        self.SomaFields()
        self.GearsWindowViewandScene()
        self.timeofGears()
        self.AllGBtns()
        self.GearsWindow.show()

#gears window functions and more:

    def GearsWindowViewandScene (self):
        
        self.SceneGears = QGraphicsScene(self.GearsWindow)
        #pixmaps prep:
        self.GPix1 = QGraphicsPixmapItem(QPixmap("beaugears"))
        self.GPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.GPix1.setScale(0.2)

        self.G2Pix = QGraphicsPixmapItem(QPixmap("gearbefore"))
        self.G2Pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.G2Pix.setScale(0.3)

        self.g3Pix = QGraphicsPixmapItem(QPixmap("gearafter"))
        self.g3Pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g3Pix.setScale(0.28)

        self.g5pix = QGraphicsPixmapItem(QPixmap("gears1"))
        self.g5pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g5pix.setScale(0.3)

        self.gear2pix = QGraphicsPixmapItem(QPixmap("gears2"))
        self.gear2pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.gear2pix.setScale(0.3)

        self.gears3pix = QGraphicsPixmapItem(QPixmap("gears3"))
        self.gears3pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.gears3pix.setScale(0.0)

        self.g4pix = QGraphicsPixmapItem(QPixmap("gears4"))
        self.g4pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g4pix.setScale(0.5)

        self.grwpix = QGraphicsPixmapItem(QPixmap("gears5"))
        self.grwpix.setFlag(QGraphicsItem.ItemIsMovable)
        self.grwpix.setScale(0.1)

        self.g6pix = QGraphicsPixmapItem(QPixmap("gears6"))
        self.g6pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g6pix.setScale(0.25)

        #pix add:
        self.SceneGears.addItem(self.GPix1)
        self.SceneGears.addItem(self.G2Pix)
        self.SceneGears.addItem(self.g3Pix)
        self.SceneGears.addItem(self.g5pix)
        self.SceneGears.addItem(self.gear2pix)
        self.SceneGears.addItem(self.gears3pix)
        self.SceneGears.addItem(self.g4pix)
        self.SceneGears.addItem(self.grwpix)
        self.SceneGears.addItem(self.g6pix)

        def GearsWinView(self):
            self.GearsView = QGraphicsView(self.SceneGears, self.GearsWindow)
            self.GearsView.setGeometry(0, 0, 500, 650)
        GearsWinView(self)

    def MWSk (self):

        self.LabelT = QLabel("Calculadora de Elementos de Máquinas", self.GearsWindow)
        self.LabelT.move(600, 0)
#def timeline and timer:
    def timeofGears(self):

        self.lineGears = QTimeLine(70000, self.GearsWindow)
        self.lineGears.setFrameRange(0, 20000)
        self.lineGears.setLoopCount(2)

        def GearsTimerfunc(self):
            self.Geartimer = QTimer()
            self.Geartimer.isSingleShot()

        GearsTimerfunc(self)

        #def animations:
        #ani1:
        def GAnime1 (self):

            self.g1ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g1ani.setTimeLine(self.lineGears)
            self.g1ani.setItem(self.GPix1)
            self.g1ani.setPosAt(0.0, QPointF(0.0, 0.0))
            self.g1ani.setScaleAt(0.0015, 1.9, 1.9)
            self.g1ani.setPosAt(0.0016, QPointF(0.0, 0.0))
            self.g1ani.setPosAt(0.0040, QPointF(-300.0, 0.0))
            self.g1ani.setPosAt(0.110, QPointF(-1400.0, 0.0))

        #ani2:

        def GA2nime (self):

            self.g2ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g2ani.setTimeLine(self.lineGears)
            self.g2ani.setItem(self.G2Pix)
            self.g2ani.setPosAt(0.0, QPointF(1200.0, 0.0))
            self.g2ani.setPosAt(0.0044, QPointF(1200.0, 0.0))
            self.g2ani.setPosAt(0.0045, QPointF(0.0, 0.0))
            self.g2ani.setScaleAt(0.0050, 1.7, 1.7)
            self.g2ani.setScaleAt(0.0055, 2.3, 2.3)
            self.g2ani.setScaleAt(0.0065, 3.0, 3.0)
            self.g2ani.setPosAt(0.0085, QPointF(-150.0, 0.0))
            self.g2ani.setPosAt(0.01, QPointF(-300.0, 0.0))
            self.g2ani.setPosAt(0.011, QPointF(-1200.0, 0.0))

        #ani3:

        def G3Ani (self):

            self.g3anim = QGraphicsItemAnimation(self.GearsWindow)
            self.g3anim.setTimeLine(self.lineGears)
            self.g3anim.setItem(self.g3Pix)
            self.g3anim.setPosAt(0.0, QPointF(800, 200))
            self.g3anim.setPosAt(0.011, QPointF(800, 200))
            self.g3anim.setPosAt(0.013, QPointF(0.0, 300))
            self.g3anim.setScaleAt(0.012, 1.0, 1.0)
            self.g3anim.setScaleAt(0.0132, 1.8, 1.8)
            self.g3anim.setScaleAt(0.015, 3.0, 3.0)
            self.g3anim.setPosAt(0.02, QPointF(0.0, 0.0))
            self.g3anim.setPosAt(0.043, QPointF(-350.0, 0.0))
            self.g3anim.setPosAt(0.094,QPointF(-1450, 0))

        #ani4:

        def G4Ani (self):

            self.g4ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g4ani.setTimeLine(self.lineGears)
            self.g4ani.setItem(self.g5pix)
            self.g4ani.setPosAt(0.0, QPointF(800, 200))
            self.g4ani.setPosAt(0.053, QPointF(800, 200))
            self.g4ani.setPosAt(0.055, QPointF(0.0, 200.0))
            self.g4ani.setScaleAt(0.075, 2.5, 2.5)
            self.g4ani.setPosAt(0.075, QPointF(0.0, 50.0))
            self.g4ani.setScaleAt(0.095, 3.7, 3.7)
            self.g4ani.setPosAt(0.095, QPointF(-50.0, -10.0))
            self.g4ani.setPosAt(0.110, QPointF(-300, -10.0))
            self.g4ani.setPosAt(0.130, QPointF(-700.0, -10.0))
            self.g4ani.setPosAt(0.175, QPointF(-1600.0, -10.0))

        def gears5Ani (self):

            self.g5ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g5ani.setTimeLine(self.lineGears)
            self.g5ani.setItem(self.gear2pix)
            self.g5ani.setPosAt(0.0, QPointF(800, 200))
            self.g5ani.setPosAt(0.110, QPointF(800, 200))
            self.g5ani.setPosAt(0.121, QPointF(0, 0))
            self.g5ani.setScaleAt(0.150, 1.6, 1.6)
            self.g5ani.setScaleAt(0.170, 3.6, 3.6)
            self.g5ani.setPosAt(0.171, QPointF(0, 0))
            self.g5ani.setPosAt(0.210, QPointF(-350, 0))
            self.g5ani.setPosAt(0.250, QPointF(-1200.0, 0))

        def gears6Ani (self):

            self.g6ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g6ani.setTimeLine(self.lineGears)
            self.g6ani.setItem(self.gears3pix)
            self.g6ani.setPosAt(0.0, QPointF(800, 200))
            self.g6ani.setPosAt(0.248, QPointF(800.0, 200.0))
            self.g6ani.setPosAt(0.255, QPointF(0.0, 0.0))
            self.g6ani.setScaleAt(0.275, 2.2, 2.2)
            self.g6ani.setPosAt(0.32, QPointF(-300.0, 0.0))
            self.g6ani.setPosAt(0.45, QPointF(-1800.0, 0.0))

        def g7Ani (self):

            self.g7ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g7ani.setTimeLine(self.lineGears)
            self.g7ani.setItem(self.g4pix)
            self.g7ani.setPosAt(0.0, QPointF(1200.0, 800))
            self.g7ani.setPosAt(0.28, QPointF(0.0, 0.0))
            self.g7ani.setScaleAt(0.30, 1.8, 1.8)
            self.g7ani.setPosAt(0.30, QPointF(0.0, 0.0))
            self.g7ani.setScaleAt(0.32, 2.5, 2.5)
            self.g7ani.setPosAt(0.37, QPointF(-420, -10))
            self.g7ani.setPosAt(0.41, QPointF(-1200, -10))

        def g8Ani (self):

            self.g8Ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g8Ani.setTimeLine(self.lineGears)
            self.g8Ani.setItem(self.grwpix)
            self.g8Ani.setPosAt(0.0, QPointF(800.0, -350.0))
            self.g8Ani.setPosAt(0.35, QPointF(800.0, -350.0))
            self.g8Ani.setPosAt(0.38, QPointF(0.0, 0.0))
            self.g8Ani.setScaleAt(0.38, 2.0, 2.0)
            self.g8Ani.setScaleAt(0.4, 4.0, 4.0)
            self.g8Ani.setPosAt(0.45, QPointF(-450.0, 0.0))
            self.g8Ani.setPosAt(0.5, QPointF(-900.0, 0.0))
            self.g8Ani.setPosAt(0.55, QPointF(-1350.0, 0.0))

        def g9ani (self):

            self.g9ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g9ani.setTimeLine(self.lineGears)
            self.g9ani.setItem(self.g6pix)
            self.g9ani.setPosAt(0.0, QPointF(800, -200))
            self.g9ani.setPosAt(0.55, QPointF(800, -200))
            self.g9ani.setPosAt(0.56, QPointF(0.0, 0.0))
            self.g9ani.setScaleAt(0.6, 3.5, 3.5)
            self.g9ani.setPosAt(0.8, QPointF(-250.0, -250.0))
            self.g9ani.setPosAt(0.98, QPointF(-650, -300.0))

        #animations finalization:
        GAnime1(self)
        GA2nime(self)
        G3Ani(self)
        G4Ani(self)
        gears5Ani(self)
        gears6Ani(self)
        g7Ani(self)
        g8Ani(self)
        g9ani(self)
        self.lineGears.start()


#test:

    def SomaFields (self):

        self.field1 = QLineEdit("teste", self.GearsWindow)
        self.field1.move(600, 20)
        self.field2 = QLineEdit("teste2", self.GearsWindow)
        self.field2.move(750, 20)
        self.Calcular = QPushButton("soma", self.GearsWindow)
        self.Calcular.move(600, 50)
        self.Calcular.clicked.connect(self.TesteSoma)
        #test:
        self.Butao = QPushButton("teste3", self.GearsWindow)
        self.Butao.move(760, 90)
        self.Butao.clicked.connect(self.WindowInWindow)

    def WindowInWindow (self):

        self.Windowisidewindow = QWidget()
        self.testLabel()
        self.Windowisidewindow.show()

    def TesteSoma (self):

        self.Input1 = self.field1.text()
        self.Input2 = self.field2.text()
        self.a = float(self.Input1)
        self.b = float(self.Input2)
        self.res = self.a + self.b
        self.ResultadoField = QLabel("teste" , self.GearsWindow)
        self.ResultadoField.setText(str(self.res))
        self.ResultadoField.move(760, 120)
        self.ResultadoField.show()
        
    def testLabel (self):

        self.testeeeee = QLabel("teste", self.Windowisidewindow)

    def AllGBtns (self):

        self.g1Btn = QPushButton("Cálculo de Dp", self.GearsWindow)
        self.g1Btn.setFont(QFont("Arial", 20, 8, True))
        self.g1Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g1Btn.move(520, 100)

        self.g2Btn = QPushButton("Cálculo de Módulo", self.GearsWindow)
        self.g2Btn.setFont(QFont("Arial", 20, 8, True))
        self.g2Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g2Btn.move(920, 100)

        self.g3Btn = QPushButton("Cálculo de De", self.GearsWindow)
        self.g3Btn.setFont(QFont("Arial", 20, 8, True))
        self.g3Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g3Btn.move(520, 150)

        self.g3Btn = QPushButton("Cálculo de h(c+f) com m", self.GearsWindow)
        self.g3Btn.setFont(QFont("Arial", 20, 8, True))
        self.g3Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g3Btn.move(820, 150)

        self.g4Btn = QPushButton("Cálculo de módulo tendo h", self.GearsWindow)
        self.g4Btn.setFont(QFont("Arial", 20, 8, True))
        self.g4Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g4Btn.move(520, 200)

        self.g5Btn = QPushButton("Cálculo de f tendo m", self.GearsWindow)
        self.g5Btn.setFont(QFont("Arial", 20, 8, True))
        self.g5Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g5Btn.move(920, 200)

        self.g6Btn = QPushButton("Cálculo de m tendo f", self.GearsWindow)
        self.g6Btn.setFont(QFont("Arial", 20, 8, True))
        self.g6Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g6Btn.move(520, 250)

        self.g7Btn = QPushButton("Cálculo de Di tendo m e Dp", self.GearsWindow)
        self.g7Btn.setFont(QFont("Arial", 20, 8, True))
        self.g7Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g7Btn.move(820, 250)

        self.g8Btn = QPushButton("Cálculo de Di tendo z e m", self.GearsWindow)
        self.g8Btn.setFont(QFont("Arial", 20, 8, True))
        self.g8Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g8Btn.move(520, 300)

        self.g9Btn = QPushButton("Cálculo de m tendo Di e z", self.GearsWindow)
        self.g9Btn.setFont(QFont("Arial", 20, 8, True))
        self.g9Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g9Btn.move(920, 300)

        self.g10Btn = QPushButton("Cálculo de passo tendo m", self.GearsWindow)
        self.g10Btn.setFont(QFont("Arial", 20, 8, True))
        self.g10Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g10Btn.move(520, 350)

        self.g11Btn = QPushButton("Cálculo de m tendo p", self.GearsWindow)
        self.g11Btn.setFont(QFont("Arial", 20, 8, True))
        self.g11Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g11Btn.move(920, 350)

        self.g12Btn = QPushButton("Cálculo de dist. entre Centros", self.GearsWindow)
        self.g12Btn.setFont(QFont("Arial", 20, 8, True))
        self.g12Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g12Btn.move(520, 400)

        self.g13Btn = QPushButton("Cálculo de m com Mt", self.GearsWindow)
        self.g13Btn.setFont(QFont("Arial", 20, 8, True))
        self.g13Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g13Btn.move(920, 400)

        self.g14Btn = QPushButton("Cálculo de Dp ECDH", self.GearsWindow)
        self.g14Btn.setFont(QFont("Arial", 20, 8, True))
        self.g14Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g14Btn.move(950, 450)

        self.g15Btn = QPushButton("Cálculo de Passo normal ECDH", self.GearsWindow)
        self.g15Btn.setFont(QFont("Arial", 20, 8, True))
        self.g15Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g15Btn.move(520, 450)

        self.g16Btn = QPushButton("Cálculo de Mn ECDH", self.GearsWindow)
        self.g16Btn.setFont(QFont("Arial", 20, 8, True))
        self.g16Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g16Btn.move(520, 500)

        self.g17Btn = QPushButton("Cálculo de Mn (De e C) ECDH", self.GearsWindow)
        self.g17Btn.setFont(QFont("Arial", 20, 8, True))
        self.g17Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g17Btn.move(820, 500)

        self.g18Btn = QPushButton("Cálculo de Âng. pressão ECDH", self.GearsWindow)
        self.g18Btn.setFont(QFont("Arial", 20, 8, True))
        self.g18Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.g18Btn.move(520, 550)

        


#########################ScrewsWindow########################################

    def CreateScrewWindow (self):

        self.ScrewWindow = QWidget()
        self.ScrewWindow.setGeometry(150, 150, 1280, 650)
        self.ScrewWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewWindow.setWindowTitle("Seção dos Parafusos")
        self.ScrewWindow.setWindowIcon(QIcon("ParafusoIcon"))
        #space for function calls
        self.ScrewSceneandView()
        self.ScrewLine()
        self.ParafBtns()
        self.ParafLabls()

        self.ScrewWindow.show()

    def ScrewSceneandView (self):

        self.ParafScene = QGraphicsScene(self.ScrewWindow)
        #pixmap prep
        self.Ppix1 = QGraphicsPixmapItem(QPixmap("screwhist1"))
        self.Ppix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.Ppix1.setScale(0.5)

        self.PPix2 = QGraphicsPixmapItem(QPixmap("screwhist2"))
        self.PPix2.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix2.setScale(0.3)

        self.PPix3 = QGraphicsPixmapItem(QPixmap("screwhist3"))
        self.PPix3.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix3.setScale(0.3)

        self.PPix4 = QGraphicsPixmapItem(QPixmap("screwhist4"))
        self.PPix4.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix4.setScale(0.3)

        self.PPIx5 = QGraphicsPixmapItem(QPixmap("screwhist5"))
        self.PPIx5.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPIx5.setScale(0.3)

        self.PPix6 = QGraphicsPixmapItem(QPixmap("screwhist6"))
        self.PPix6.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix6.setScale(0.4)

        self.PPix7 = QGraphicsPixmapItem(QPixmap("screwhist7"))
        self.PPix7.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix7.setScale(0.4)
        

        self.PPix8 = QGraphicsPixmapItem(QPixmap("screwhist8"))
        self.PPix8.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix8.setScale(0.3)

        self.PPix9 = QGraphicsPixmapItem(QPixmap("screwhist9"))
        self.PPix9.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix9.setScale(0.35)

        self.PPix10 = QGraphicsPixmapItem(QPixmap("screwhist10"))
        self.PPix10.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix10.setScale(0.4)

        self.PPix11 = QGraphicsPixmapItem(QPixmap("screwhist11"))
        self.PPix11.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix11.setScale(0.4)

        self.PPix12 = QGraphicsPixmapItem(QPixmap("screwhist12"))
        self.PPix12.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix12.setScale(0.4)

        self.PPix13 = QGraphicsPixmapItem(QPixmap("screwhist13"))
        self.PPix13.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix13.setScale(0.4)



        #pix add
        self.ParafScene.addItem(self.Ppix1)
        self.ParafScene.addItem(self.PPix2)
        self.ParafScene.addItem(self.PPix3)
        self.ParafScene.addItem(self.PPix4)
        self.ParafScene.addItem(self.PPIx5)
        self.ParafScene.addItem(self.PPix6)
        self.ParafScene.addItem(self.PPix7)
        self.ParafScene.addItem(self.PPix8)
        self.ParafScene.addItem(self.PPix9)
        self.ParafScene.addItem(self.PPix10)
        self.ParafScene.addItem(self.PPix11)
        self.ParafScene.addItem(self.PPix12)
        self.ParafScene.addItem(self.PPix13)


        #view def
        def ScrewWindowView (self):

            ParafView = QGraphicsView(self.ParafScene, self.ScrewWindow)
            ParafView.setGeometry(0, 0, 500, 650)

        ScrewWindowView(self)

#def timeline and timer:

    def ScrewLine (self):

        self.linhaparaf = QTimeLine(70000, self.ScrewWindow)
        self.linhaparaf.setFrameRange(0, 20000)
        self.linhaparaf.setLoopCount(0)
        def ScrewTimer (self):
            self.parafusotimer = QTimer()
            self.parafusotimer.isSingleShot()
        ScrewTimer(self)
        #def animations:
        #ani1:

        def SAnim1 (self):

            self.sani1 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani1.setTimeLine(self.linhaparaf)
            self.sani1.setItem(self.Ppix1)
            self.sani1.setPosAt(0.0, QPointF(32.0, 0.0))
            self.sani1.setPosAt(0.02, QPointF(-750, 0.0))

        def SAnim2 (self):

            self.sani2 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani2.setTimeLine(self.linhaparaf)
            self.sani2.setItem(self.PPix2)
            self.sani2.setPosAt(0.0, QPointF(1000.0, 0.0))
            self.sani2.setScaleAt(0.0155, 2.1, 2.1)
            self.sani2.setPosAt(0.02, QPointF(0.0, 0.0))
            self.sani2.setPosAt(0.04, QPointF(-1000.0, 0.0))

        def SAnim3 (self):

            self.sani3 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani3.setTimeLine(self.linhaparaf)
            self.sani3.setItem(self.PPix3)
            self.sani3.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani3.setScaleAt(0.025, 2.5, 2.5)
            self.sani3.setPosAt(0.04, QPointF(0.0, 0.0))
            self.sani3.setPosAt(0.06, QPointF(-1100.0, 0.0))

        def SAnim4 (self):

            self.sani4 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani4.setTimeLine(self.linhaparaf)
            self.sani4.setItem(self.PPix4)
            self.sani4.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani4.setScaleAt(0.035, 3.0, 3.0)
            self.sani4.setPosAt(0.065, QPointF(200.0, 0.0))
            self.sani4.setPosAt(0.095, QPointF(-1300.0, 0.0))

        def SAnim5 (self):

            self.sani5 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani5.setTimeLine(self.linhaparaf)
            self.sani5.setItem(self.PPIx5)
            self.sani5.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani5.setScaleAt(0.07, 2.8, 2.8)
            self.sani5.setPosAt(0.099, QPointF(500.0, 0.0))
            self.sani5.setPosAt(0.15, QPointF(-500.0, 0.0))
            self.sani5.setPosAt(0.2, QPointF(-1800.0, 0.0))

        def SAnim6 (self):

            self.sani6 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani6.setTimeLine(self.linhaparaf)
            self.sani6.setItem(self.PPix6)
            self.sani6.setPosAt(0.0, QPointF(1000.0, 0.0))
            self.sani6.setPosAt(0.14, QPointF(850.0, 0.0))
            self.sani6.setScaleAt(0.145, 2.1, 2.1)
            self.sani6.setPosAt(0.2, QPointF(0.0, 0.0))
            self.sani6.setPosAt(0.23, QPointF(-100.0, 0.0))
            self.sani6.setPosAt(0.28, QPointF(-1500.0, 0.0))

        def ScrewAnim7 (self):

            self.sani7 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani7.setTimeLine(self.linhaparaf)
            self.sani7.setItem(self.PPix7)
            self.sani7.setPosAt(0.0, QPointF(1800.0, 0.0))
            self.sani7.setPosAt(0.028, QPointF(1800.0, 0.0))
            self.sani7.setScaleAt(0.32, 1.55, 1.55)
            self.sani7.setPosAt(0.33, QPointF(0.0, 0.0))
            self.sani7.setPosAt(0.35, QPointF(-1500.0, 0.0))

        def ScrAni8 (self):

            self.sani8 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani8.setTimeLine(self.linhaparaf)
            self.sani8.setItem(self.PPix8)
            self.sani8.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani8.setScaleAt(0.35, 2.7, 2.7)
            self.sani8.setPosAt(0.034, QPointF(1500.0, 0.0))
            self.sani8.setPosAt(0.35, QPointF(800.0, 0.0))
            self.sani8.setPosAt(0.365, QPointF(100.0, 0.0))
            self.sani8.setPosAt(0.49, QPointF(-1400.0, 0.0))

        def ScrAni9 (self):

            self.sani9 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani9.setTimeLine(self.linhaparaf)
            self.sani9.setItem(self.PPix9)
            self.sani9.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani9.setScaleAt(0.35, 1.0, 1.0)
            self.sani9.setPosAt(0.3, QPointF(1200.0, 0.0))
            self.sani9.setScaleAt(0.36, 2.1, 2.1)
            self.sani9.setPosAt(0.50, QPointF(100.0, 0.0))
            self.sani9.setPosAt(0.59, QPointF(-1400.0, 0.0))

        def ScrAni10 (self):

            self.sani10 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani10.setTimeLine(self.linhaparaf)
            self.sani10.setItem(self.PPix10)
            self.sani10.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani10.setScaleAt(0.4, 1.0, 1.0)
            self.sani10.setPosAt(0.49, QPointF(1200.0, 0.0))
            self.sani10.setScaleAt(0.49, 2.1, 2.1)
            self.sani10.setPosAt(0.59, QPointF(100.0, 0.0))
            self.sani10.setPosAt(0.63, QPointF(-300.0, 0.0))
            self.sani10.setPosAt(0.69, QPointF(-1250.0, 0.0))

        def ScrAni11 (self):

            self.sani11 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani11.setTimeLine(self.linhaparaf)
            self.sani11.setItem(self.PPix11)
            self.sani11.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani11.setScaleAt(0.5, 1.0, 1.0)
            self.sani11.setPosAt(0.5, QPointF(1500.0, 0.0))
            self.sani11.setScaleAt(0.59, 2.1, 2.1)
            self.sani11.setPosAt(0.68, QPointF(1500.0, 0.0))
            self.sani11.setPosAt(0.69, QPointF(100.0, 0.0))
            self.sani11.setPosAt(0.73, QPointF(-300.0, 0.0))
            self.sani11.setPosAt(0.79, QPointF(-1250.0, 0.0))

        def ScrAni12 (self):

            self.sani12 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani12.setTimeLine(self.linhaparaf)
            self.sani12.setItem(self.PPix12)
            self.sani12.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani12.setScaleAt(0.63, 2.4, 2.4)
            self.sani12.setPosAt(0.73, QPointF(1500.0, 0.0))
            self.sani12.setPosAt(0.79, QPointF(100.0, 0.0))
            self.sani12.setPosAt(0.86, QPointF(-1450.0, 0.0))

        def ScrFinal (self):

            self.sani13 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani13.setTimeLine(self.linhaparaf)
            self.sani13.setItem(self.PPix13)
            self.sani13.setPosAt(0.0, QPointF(1500.0 , 0.0))
            self.sani13.setPosAt(0.86, QPointF(1500.0, 0.0))
            self.sani13.setScaleAt(0.83, 2.5, 2.5)
            self.sani13.setPosAt(0.87, QPointF(-100.0, 0.0))
            self.sani13.setPosAt(0.91, QPointF(-490.0, 0.0))
            self.sani13.setPosAt(0.95, QPointF(-550.0, 0.0))
            self.sani13.setPosAt(1.0, QPointF(-1200.0, 0.0))


        #animations finalization:
        SAnim1(self)
        SAnim2(self)
        SAnim3(self)
        SAnim4(self)
        SAnim5(self)
        SAnim6(self)
        ScrewAnim7(self)
        ScrAni8(self)
        ScrAni9(self)
        ScrAni10(self)
        ScrAni11(self)
        ScrAni12(self)
        ScrFinal(self)
        self.linhaparaf.start()

#screwWindowBtns:

    def ParafBtns (self):

        self.P1Btn = QPushButton("Conversão Tn Tcis", self.ScrewWindow)
        self.P1Btn.setFont(QFont("Arial", 20, 8, True))
        self.P1Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P1Btn.move(520, 225)
        self.P1Btn.clicked.connect(self.ScrewCalc1)


        self.P2Btn = QPushButton("Conversão Tcis Tn", self.ScrewWindow)
        self.P2Btn.setFont(QFont("Arial", 20, 8, True))
        self.P2Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P2Btn.move(920, 225)
        self.P2Btn.clicked.connect(self.ScrewCalc2)


        self.P3Btn = QPushButton("Conversão MPa Kgf", self.ScrewWindow)
        self.P3Btn.setFont(QFont("Arial", 20, 8, True))
        self.P3Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P3Btn.move(520, 300)
        self.P3Btn.clicked.connect(self.ScrewCalc3)


        self.P4Btn = QPushButton("Conversão Kgf MPa", self.ScrewWindow)
        self.P4Btn.setFont(QFont("Arial", 20, 8, True))
        self.P4Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P4Btn.move(920, 300)
        self.P4Btn.clicked.connect(self.ScrewCalc4)


        self.P5Btn = QPushButton("Área Circular", self.ScrewWindow)
        self.P5Btn.setFont(QFont("Arial", 20, 8, True))
        self.P5Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P5Btn.move(520, 375)
        self.P5Btn.clicked.connect(self.ScrewCalc5)


        self.P6Btn = QPushButton("Cálculo Tensão MPa", self.ScrewWindow)
        self.P6Btn.setFont(QFont("Arial", 20, 8, True))
        self.P6Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P6Btn.move(920, 375)
        self.P6Btn.clicked.connect(self.ScrewCalc6)


        self.P7Btn = QPushButton("Cálculo Tensão Kgf", self.ScrewWindow)
        self.P7Btn.setFont(QFont("Arial", 20, 8, True))
        self.P7Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P7Btn.move(520, 450)
        self.P7Btn.clicked.connect(self.ScrewCalc7)


        self.P8Btn = QPushButton("Cálculo de raio MPa", self.ScrewWindow)
        self.P8Btn.setFont(QFont("Arial", 20, 8, True))
        self.P8Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P8Btn.move(920, 450)
        self.P8Btn.clicked.connect(self.ScrewCalc8)



        self.P9Btn = QPushButton("Cálculo raio Kgf", self.ScrewWindow)
        self.P9Btn.setFont(QFont("Arial", 20, 8, True))
        self.P9Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P9Btn.move(520, 525)
        self.P9Btn.clicked.connect(self.ScrewCalc9)

        self.P10Btn = QPushButton("Parafusos para n pontos", self.ScrewWindow)
        self.P10Btn.setFont(QFont("Arial", 20, 8, True))
        self.P10Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P10Btn.move(820, 525)
        self.P10Btn.clicked.connect(self.ScrewCalc10)


        self.P11Btn = QPushButton("força suportável por n parafusos", self.ScrewWindow)
        self.P11Btn.setFont(QFont("Arial", 20, 8, True))
        self.P11Btn.setStyleSheet("color: rgb(17, 11, 26)")
        self.P11Btn.move(520, 600)
        self.P11Btn.clicked.connect(self.ScrewCalc11)

#Labels:

    def ParafLabls (self):

        self.PLlabel1 = QLabel("Lengenda:", self.ScrewWindow)
        self.PLlabel1.setFont(QFont("Arial", 20, 8, True))
        self.PLlabel1.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel1.move(510.0, 0.0)

        self.PLlabel2 = QLabel("Tcis = Tensão de cisalhamento", self.ScrewWindow)
        self.PLlabel2.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel2.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel2.move(510.0, 30.0)

        self.PLlabel3 = QLabel("Tn = Tensão Normal", self.ScrewWindow)
        self.PLlabel3.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel3.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel3.move(510.0, 50.0)

        self.PLlabel4 = QLabel("clique em info(i) para ver a fórmula", self.ScrewWindow)
        self.PLlabel4.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel4.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel4.move(510.0, 70.0)

        self.PLlabel5 = QLabel("clique em SI[ ] para ver o sistema de unidades", self.ScrewWindow)
        self.PLlabel5.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel5.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel5.move(510.0, 90.0)

        self.PLlabel6 = QLabel("Utilize sempre ponto '.' para casas decimais", self.ScrewWindow)
        self.PLlabel6.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel6.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel6.move(510.0, 110.0)

        self.PLlabel7 = QLabel("Clique em notes para fazer anotações de resultados ", self.ScrewWindow)
        self.PLlabel7.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel7.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel7.move(510.0, 130.0)

        self.PLlabel8 = QLabel("Clique em formulário para ver as fórmulas", self.ScrewWindow)
        self.PLlabel8.setFont(QFont("Arial", 16, 8, True))
        self.PLlabel8.setStyleSheet("color: rgb(17, 11, 26)")
        self.PLlabel8.move(510.0, 150.0)

        self.PLnotes = QPushButton("Notes", self.ScrewWindow)
        self.PLnotes.setFont(QFont("Arial", 16, 8, True))
        self.PLnotes.setStyleSheet("color: rgb(17, 11, 26); background-color: white")
        self.PLnotes.move(850.0, 5.0)
        self.PLnotes.clicked.connect(self.FNotes)

        self.PLinfo1 = QPushButton("Formulário", self.ScrewWindow)
        self.PLinfo1.setFont(QFont("Arial", 14, 8, True))
        self.PLinfo1.setStyleSheet("color: rgb(17, 11, 26); background-color: white")
        self.PLinfo1.move(805.0, 180.0)
        self.PLinfo1.clicked.connect(self.Screwinfo)

#########Screw Window Functions:


    def FNotes (self):

        self.PNotes = QLineEdit("anotações", self.ScrewWindow)
        self.PNotes.move(995.0, 5.0)
        self.PNotes.setStyleSheet("color: rgb(17, 11, 26); background-color: white")
        self.PNotes.setFont(QFont("Arial", 14, 8, True))
        self.PNotes.setGeometry(995.0, 5.0, 270.0, 150.0)
        self.PNotes.show()

    def Screwinfo (self):

        self.ScrewInfoWindow = QWidget()
        self.ScrewInfoWindow.setGeometry(150, 180, 500, 600)
        self.ScrewInfoWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewInfoWindow.setWindowTitle("Formulário")
        self.ScrInfoLabel()
        self.ScrewInfoWindow.show()

    def ScrInfoLabel (self):

        self.FormularioLabel = QLabel("segue formulário", self.ScrewInfoWindow)
        self.FormPixmap = QPixmap("formulárioParaf")
        self.FormularioLabel.setPixmap(self.FormPixmap)

    def ScrewCalc1 (self):

        self.ScrewCalcW1 = QWidget()
        self.ScrewCalcW1.setWindowIcon(QIcon("calcIcon"))
        self.ScrewCalcW1.setGeometry(550, 180, 700, 300)
        self.ScrewCalcW1.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW1.setWindowTitle("Conversão Tn Tcis")
        self.ScrCalc1Front()
        self.ScrewCalcW1.show()


    def ScrCalc1Front (self):

        self.TnTcis = QLineEdit("Digite Tn", self.ScrewCalcW1)
        self.TnTcis.setFont(QFont("Arial", 20, 8, True))
        self.TnTcis.setStyleSheet("color: rgb(17, 11, 26)")
        self.TnTcis.move(100.0, 40.0)

        self.TnTCisBtn = QPushButton("Calcular Tcis", self.ScrewCalcW1)
        self.TnTCisBtn.setFont(QFont("Arial", 20, 8, True))
        self.TnTCisBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.TnTCisBtn.move(100.0, 100.0)
        self.TnTCisBtn.clicked.connect(self.CalcTnTcis)

    def CalcTnTcis (self):

        self.Input1 = self.TnTcis.text()
        self.VarTnTcis = float(self.Input1)
        self.ResVarTnTcis = self.VarTnTcis * 0.7        
        self.TestQline = QLineEdit(self.ScrewCalcW1)
        self.TestQline.setText(str(self.ResVarTnTcis) +  "   [MPa] ou [Kgf/mm²]")
        self.TestQline.setFont(QFont("Arial", 20, 8, True))
        self.TestQline.setStyleSheet("color: rgb(0, 0, 0)")
        self.TestQline.move(100.0, 160.0)
        self.TestQline.setGeometry(100, 160, 380, 40)
        self.TestQline.show()


    def ScrewCalc2 (self):

        self.ScrewCalcW2 = QWidget()
        self.ScrewCalcW2.setWindowIcon(QIcon("calcIcon"))
        self.ScrewCalcW2.setGeometry(550, 180, 700, 300)
        self.ScrewCalcW2.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW2.setWindowTitle("Conversão Tcis Tn")
        self.ScrCalc2Front()
        self.ScrewCalcW2.show()

    def ScrCalc2Front (self):

        self.TcisTn = QLineEdit("Digite Tcis", self.ScrewCalcW2)
        self.TcisTn.setFont(QFont("Arial", 20, 8, True))
        self.TcisTn.setStyleSheet("color: rgb(17, 11, 26)")
        self.TcisTn.move(100.0, 40.0)

        self.TcisTnBtn = QPushButton("Calcular Tn", self.ScrewCalcW2)
        self.TcisTnBtn.setFont(QFont("Arial", 20, 8, True))
        self.TcisTnBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.TcisTnBtn.move(100.0, 100.0)
        self.TcisTnBtn.clicked.connect(self.CalcTcisTn)

    def CalcTcisTn (self):

        self.Input2 = self.TcisTn.text()
        self.VarTcisTn = float(self.Input2)
        self.ResVarTcisTn = self.VarTcisTn * 1.428571428571429        
        self.ResQline = QLineEdit(self.ScrewCalcW2)
        self.ResQline.setText(str(self.ResVarTcisTn) +  "   [MPa] ou [Kgf/mm²]")
        self.ResQline.setFont(QFont("Arial", 20, 8, True))
        self.ResQline.setStyleSheet("color: rgb(0, 0, 0)")
        self.ResQline.move(100.0, 160.0)
        self.ResQline.setGeometry(100, 160, 550, 40)
        self.ResQline.show()
        

    def ScrewCalc3 (self):

        self.ScrewCalcW3 = QWidget()
        self.ScrewCalcW3.setWindowIcon(QIcon("calcIcon"))
        self.ScrewCalcW3.setGeometry(550, 180, 700, 300)
        self.ScrewCalcW3.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW3.setWindowTitle("Conversão MPa Kgf")
        self.ScrewCalc3Front()
        self.ScrewCalcW3.show()

    def ScrewCalc3Front (self):

        self.MPaKgf = QLineEdit("Digite valor MPa", self.ScrewCalcW3)
        self.MPaKgf.setFont(QFont("Arial", 20, 8, True))
        self.MPaKgf.setStyleSheet("color: rgb(17, 11, 26)")
        self.MPaKgf.move(100.0, 40.0)

        self.MPaKgfBtn = QPushButton("Calcular Kgf", self.ScrewCalcW3)
        self.MPaKgfBtn.setFont(QFont("Arial", 20, 8, True))
        self.MPaKgfBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.MPaKgfBtn.move(100.0, 100.0)
        self.MPaKgfBtn.clicked.connect(self.CalcMPaKgf)

    def CalcMPaKgf (self):

        self.Input3 = self.MPaKgf.text()
        self.VarMPaKgf = float(self.Input3)
        self.ResVarMPaKgf = self.VarMPaKgf * 0.101972
        self.RMPAKgf = QLineEdit(self.ScrewCalcW3)
        self.RMPAKgf.setText(str(self.ResVarMPaKgf) +  "   [Kgf/mm²]")
        self.RMPAKgf.setFont(QFont("Arial", 20, 8, True))
        self.RMPAKgf.setStyleSheet("color: rgb(0, 0, 0)")
        self.RMPAKgf.move(100.0, 160.0)
        self.RMPAKgf.setGeometry(100, 160, 450, 40)
        self.RMPAKgf.show()

    def ScrewCalc4 (self):

        self.ScrewCalcW4 = QWidget()
        self.ScrewCalcW4.setWindowIcon(QIcon("calcIcon"))
        self.ScrewCalcW4.setGeometry(550, 180, 700, 300)
        self.ScrewCalcW4.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW4.setWindowTitle("Conversão Kgf MPa")
        self.ScrewCalc4Front()
        self.ScrewCalcW4.show()

    def ScrewCalc4Front (self):

        self.KgfMPa = QLineEdit("Digite valor Kgf", self.ScrewCalcW4)
        self.KgfMPa.setFont(QFont("Arial", 20, 8, True))
        self.KgfMPa.setStyleSheet("color: rgb(17, 11, 26)")
        self.KgfMPa.move(100.0, 40.0)

        self.KgfMPaBtn = QPushButton("Calcular MPa", self.ScrewCalcW4)
        self.KgfMPaBtn.setFont(QFont("Arial", 20, 8, True))
        self.KgfMPaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.KgfMPaBtn.move(100.0, 100.0)
        self.KgfMPaBtn.clicked.connect(self.CalcKgfMPa)

    def CalcKgfMPa (self):

        self.Input4 = self.KgfMPa.text()
        self.VarKgfMPa = float(self.Input4)
        self.ResVarKgfMPa = self.VarKgfMPa * 9.80665
        self.RKgfMPa = QLineEdit(self.ScrewCalcW4)
        self.RKgfMPa.setText(str(self.ResVarKgfMPa) + " [MPa]")
        self.RKgfMPa.setFont(QFont("Arial", 20, 8, True))
        self.RKgfMPa.setStyleSheet("color: rgb(17, 11, 26)")
        self.RKgfMPa.move(100.0, 160.0)
        self.RKgfMPa.setGeometry(100, 160, 450, 40)
        self.RKgfMPa.show()
        


    def ScrewCalc5 (self):

        self.ScrewCalcW5 = QWidget()
        self.ScrewCalcW5.setWindowIcon(QIcon("calcIcon"))
        self.ScrewCalcW5.setGeometry(550, 180, 700, 300)
        self.ScrewCalcW5.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW5.setWindowTitle("Área Circular")
        self.ScrewCalc5Front()
        self.ScrewCalcW5.show()

    def ScrewCalc5Front (self):

        self.raio = QLineEdit("Digite o raio em mm", self.ScrewCalcW5)
        self.raio.setFont(QFont("Arial", 20, 8, True))
        self.raio.setStyleSheet("color: rgb(17, 11, 26)")
        self.raio.move(100.0, 40.0)

        self.AreaBtn = QPushButton("Calcular Área", self.ScrewCalcW5)
        self.AreaBtn.setFont(QFont("Arial", 20, 8, True))
        self.AreaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.AreaBtn.move(100.0, 100.0)
        self.AreaBtn.clicked.connect(self.CalcArea)

    def CalcArea (self):

        self.Input5 = self.raio.text()
        self.raioVar = float(self.Input5)
        self.RespRaioVar = (self.raioVar * self.raioVar) * 3.14159265359
        self.Rraio = QLineEdit(self.ScrewCalcW5)
        self.Rraio.setText(str(self.RespRaioVar) + "[mm²]")
        self.Rraio.setFont(QFont("Arial", 20, 8, True))
        self.Rraio.setStyleSheet("color: rgb(17, 11, 26)")
        self.Rraio.move(100.0, 160.0)
        self.Rraio.setGeometry(100, 160, 450, 40)
        self.Rraio.show()
        

    def ScrewCalc6 (self):

        self.ScrewCalcW6 = QWidget()
        self.ScrewCalcW6.setGeometry(550, 180, 750, 320)
        self.ScrewCalcW6.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW6.setWindowTitle("Cálculo Tensão em MPa")
        self.ScrewCalc6Front()
        self.ScrewCalcW6.show()

    def ScrewCalc6Front (self):

        self.Forca = QLineEdit("digite a força em MPa", self.ScrewCalcW6)
        self.Forca.setFont(QFont("Arial", 20, 8, True))
        self.Forca.setStyleSheet("color: rgb(17, 11, 26)")
        self.Forca.setGeometry(0, 0, 350, 40)
        self.Forca.move(100.0, 40.0)

        try : self.Area = QLineEdit(str(self.RespRaioVar), self.ScrewCalcW6)
        except : self.Area = QLineEdit("Digite a Área[mm²]", self.ScrewCalcW6)
        
        self.Area.setFont(QFont("Arial", 20, 8, True))
        self.Area.setStyleSheet("color: rgb(17, 11, 26)")
        self.Area.setGeometry(0, 0, 350, 40)
        self.Area.move(100.0, 100.0)

        self.TMPaBtn = QPushButton("Calcular Tensão", self.ScrewCalcW6)
        self.TMPaBtn.setFont(QFont("Arial", 20, 8, True))
        self.TMPaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.TMPaBtn.move(100.0, 160.0)
        self.TMPaBtn.clicked.connect(self.CalcTensaoMPa)


    def CalcTensaoMPa (self):

        self.Input6 = self.Forca.text()
        self.VarForca = float(self.Input6)
        self.Input7 = self.Area.text()
        self.VarArea = float(self.Input7)
        self.TensaoMPa = self.VarForca / self.VarArea

        self.RTensaoMPa = QLineEdit(self.ScrewCalcW6)
        self.RTensaoMPa.setText(str(self.TensaoMPa) + "  [MPa] ou [N/mm²]")
        self.RTensaoMPa.setFont(QFont("Arial", 20, 8, True))
        self.RTensaoMPa.setStyleSheet("color: rgb(17, 11, 26)")
        self.RTensaoMPa.setGeometry(100, 220, 550, 40)
        self.RTensaoMPa.move(100.0, 220.0)
        self.RTensaoMPa.show()
        
        
        

    def ScrewCalc7 (self):

        self.ScrewCalcW7 = QWidget()
        self.ScrewCalcW7.setWindowIcon(QIcon("calcIcon"))
        self.ScrewCalcW7.setGeometry(550, 180, 500, 400)
        self.ScrewCalcW7.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW7.setWindowTitle("Cálculo Tensão Kgf")
        self.ScrewCalc7Front()
        self.ScrewCalcW7.show()

    def ScrewCalc7Front (self):

        self.Forca1 = QLineEdit("digite a força em Kgf", self.ScrewCalcW7)
        self.Forca1.setFont(QFont("Arial", 20, 8, True))
        self.Forca1.setStyleSheet("color: rgb(17, 11, 26)")
        self.Forca1.setGeometry(0, 0, 350, 40)
        self.Forca1.move(100.0, 40.0)

        self.Area1 = QLineEdit("digite a Área em mm²", self.ScrewCalcW7)
        self.Area1.setFont(QFont("Arial", 20, 8, True))
        self.Area1.setStyleSheet("color: rgb(17, 11, 26)")
        self.Area1.setGeometry(0, 0, 350, 40)
        self.Area1.move(100.0, 100.0)

        self.TMPaBtn1 = QPushButton("Calcular Tensão", self.ScrewCalcW7)
        self.TMPaBtn1.setFont(QFont("Arial", 20, 8, True))
        self.TMPaBtn1.setStyleSheet("color: rgb(17, 11, 26)")
        self.TMPaBtn1.move(100.0, 160.0)
        self.TMPaBtn1.clicked.connect(self.CalcTensaoKgf)


    def CalcTensaoKgf (self):

        self.Input8 = self.Forca1.text()
        self.VarForca1 = float(self.Input8)
        self.Input9 = self.Area1.text()
        self.VarArea1 = float(self.Input9)
        self.TensaoKgf = self.VarForca1 / self.VarArea1

        self.RTensaoKgf = QLabel(self.ScrewCalcW7)
        self.RTensaoKgf.setText(str(self.TensaoKgf))
        self.RTensaoKgf.setFont(QFont("Arial", 20, 8, True))
        self.RTensaoKgf.setStyleSheet("color: rgb(17, 11, 26)")
        self.RTensaoKgf.move(100.0, 220.0)
        self.RTensaoKgf.show()

        self.RTensaoKgfLabel1 = QLabel("[Kgf/mm²]", self.ScrewCalcW7)
        self.RTensaoKgfLabel1.setFont(QFont("Arial", 20, 8, True))
        self.RTensaoKgfLabel1.setStyleSheet("color: rgb(17, 11, 26)")
        self.RTensaoKgfLabel1.move(100.0, 280.0)
        self.RTensaoKgfLabel1.show()

    def ScrewCalc8 (self):

        self.ScrewCalcW8 = QWidget()
        self.ScrewCalcW8.setGeometry(550, 180, 500, 550)
        self.ScrewCalcW8.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW8.setWindowTitle("Cálculo de raio MPa")
        self.CalcraioMPaFront()
        self.ScrewCalcW8.show()

    def CalcraioMPaFront (self):

        self.ForcaSup1 = QLineEdit("digite a força em MPa", self.ScrewCalcW8)
        self.ForcaSup1.setFont(QFont("Arial", 20, 8, True))
        self.ForcaSup1.setStyleSheet("color: rgb(17, 11, 26)")
        self.ForcaSup1.setGeometry(0, 0, 350, 40)
        self.ForcaSup1.move(100.0, 40.0)

        self.Tadm1 = QLineEdit("digite a Tensão adm em MPa", self.ScrewCalcW8)
        self.Tadm1.setFont(QFont("Arial", 20, 8, True))
        self.Tadm1.setStyleSheet("color: rgb(17, 11, 26)")
        self.Tadm1.setGeometry(0, 0, 380, 40)
        self.Tadm1.move(100.0, 100.0)

        self.raioBtn2 = QPushButton("Calcular raio e diametro", self.ScrewCalcW8)
        self.raioBtn2.setFont(QFont("Arial", 20, 8, True))
        self.raioBtn2.setStyleSheet("color: rgb(17, 11, 26)")
        self.raioBtn2.move(100.0, 160.0)
        self.raioBtn2.clicked.connect(self.CalcraioMPa)

    def CalcraioMPa (self):

        self.Input12 = self.ForcaSup1.text()
        self.VarForcaSup1 = float(self.Input12)
        self.Input13 = self.Tadm1.text()
        self.VarTadm1 = float(self.Input13)
        self.RespRaioKgf11 = 3.14159265359 * self.VarTadm1
        self.RespRaioKgf22 = (self.VarForcaSup1 / self.RespRaioKgf11)**(1/2)
        self.RespRaioKgf33 = self.RespRaioKgf22 * 2

        self.RespRaioKgfLabel1 = QLabel(self.ScrewCalcW8)
        self.RespRaioKgfLabel1.setText(str(self.RespRaioKgf22))
        self.RespRaioKgfLabel1.setFont(QFont("Arial", 20, 8, True))
        self.RespRaioKgfLabel1.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespRaioKgfLabel1.move(100.0, 220.0)
        self.RespRaioKgfLabel1.show()

        self.RespRaioKgfLabel22 = QLabel("[mm], e diâmetro =", self.ScrewCalcW8)
        self.RespRaioKgfLabel22.setFont(QFont("Arial", 20, 8, True))
        self.RespRaioKgfLabel22.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespRaioKgfLabel22.move(100.0, 280.0)
        self.RespRaioKgfLabel22.show()

        self.RespRaioKgfLabel33 = QLabel(self.ScrewCalcW8)
        self.RespRaioKgfLabel33.setText(str(self.RespRaioKgf33))
        self.RespRaioKgfLabel33.setFont(QFont("Arial", 20, 8, True))
        self.RespRaioKgfLabel33.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespRaioKgfLabel33.move(100.0, 340.0)
        self.RespRaioKgfLabel33.show()

    def ScrewCalc9 (self):

        self.ScrewCalcW9 = QWidget()
        self.ScrewCalcW9.setGeometry(550, 180, 500, 550)
        self.ScrewCalcW9.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW9.setWindowTitle("Cálculo de raio Kgf")
        self.CalcraioKgfFront()
        self.ScrewCalcW9.show()

    def CalcraioKgfFront (self):

        self.ForcaSup = QLineEdit("digite a força em Kgf", self.ScrewCalcW9)
        self.ForcaSup.setFont(QFont("Arial", 20, 8, True))
        self.ForcaSup.setStyleSheet("color: rgb(17, 11, 26)")
        self.ForcaSup.setGeometry(0, 0, 350, 40)
        self.ForcaSup.move(100.0, 40.0)

        self.Tadm = QLineEdit("digite a Tensão adm Kgf", self.ScrewCalcW9)
        self.Tadm.setFont(QFont("Arial", 20, 8, True))
        self.Tadm.setStyleSheet("color: rgb(17, 11, 26)")
        self.Tadm.setGeometry(0, 0, 350, 40)
        self.Tadm.move(100.0, 100.0)

        self.raioBtn1 = QPushButton("Calcular raio e diametro", self.ScrewCalcW9)
        self.raioBtn1.setFont(QFont("Arial", 20, 8, True))
        self.raioBtn1.setStyleSheet("color: rgb(17, 11, 26)")
        self.raioBtn1.move(100.0, 160.0)
        self.raioBtn1.clicked.connect(self.CalcraioKgf)

    def CalcraioKgf (self):

        self.Input10 = self.ForcaSup.text()
        self.VarForcaSup = float(self.Input10)
        self.Input11 = self.Tadm.text()
        self.VarTadm = float(self.Input11)
        self.RespRaioKgf1 = 3.14159265359 * self.VarTadm
        self.RespRaioKgf2 = (self.VarForcaSup / self.RespRaioKgf1)**(1/2)
        self.RespRaioKgf3 = self.RespRaioKgf2 * 2

        self.RespRaioKgfLabel = QLabel(self.ScrewCalcW9)
        self.RespRaioKgfLabel.setText(str(self.RespRaioKgf2))
        self.RespRaioKgfLabel.setFont(QFont("Arial", 20, 8, True))
        self.RespRaioKgfLabel.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespRaioKgfLabel.move(100.0, 220.0)
        self.RespRaioKgfLabel.show()

        self.RespRaioKgfLabel2 = QLabel("[mm], e diâmetro =", self.ScrewCalcW9)
        self.RespRaioKgfLabel2.setFont(QFont("Arial", 20, 8, True))
        self.RespRaioKgfLabel2.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespRaioKgfLabel2.move(100.0, 280.0)
        self.RespRaioKgfLabel2.show()

        self.RespRaioKgfLabel3 = QLabel(self.ScrewCalcW9)
        self.RespRaioKgfLabel3.setText(str(self.RespRaioKgf3))
        self.RespRaioKgfLabel3.setFont(QFont("Arial", 20, 8, True))
        self.RespRaioKgfLabel3.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespRaioKgfLabel3.move(100.0, 340.0)
        self.RespRaioKgfLabel3.show()


    def ScrewCalc10 (self):

        self.ScrewCalcW10 = QWidget()
        self.ScrewCalcW10.setGeometry(550, 180, 500, 640)
        self.ScrewCalcW10.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW10.setWindowTitle("Parafusos para n pontos")
        self.ParafusosPnPontosFront()
        self.ScrewCalcW10.show()

    def ParafusosPnPontosFront (self):

        self.Tensao = QLineEdit("digite a Tensão", self.ScrewCalcW10)
        self.Tensao.setFont(QFont("Arial", 20, 8, True))
        self.Tensao.setStyleSheet("color: rgb(17, 11, 26)")
        self.Tensao.setGeometry(0, 0, 350.0, 40.0)
        self.Tensao.move(100.0, 40.0)

        self.ForcaMPKg = QLineEdit("digite a força", self.ScrewCalcW10)
        self.ForcaMPKg.setFont(QFont("Arial", 20, 8, True))
        self.ForcaMPKg.setStyleSheet("color: rgb(17, 11, 26)")
        self.ForcaMPKg.setGeometry(0, 0, 350.0, 40.0)
        self.ForcaMPKg.move(100.0, 100.0)

        self.Pontos = QLineEdit("digite o Nº de Pontos", self.ScrewCalcW10)
        self.Pontos.setFont(QFont("Arial", 20, 8, True))
        self.Pontos.setStyleSheet("color: rgb(17, 11, 26)")
        self.Pontos.setGeometry(0, 0, 350.0, 40.0)
        self.Pontos.move(100.0, 160.0)

        self.FatorSeg = QLineEdit("digite o fator de segurança", self.ScrewCalcW10)
        self.FatorSeg.setFont(QFont("Arial", 20, 8, True))
        self.FatorSeg.setStyleSheet("color: rgb(17, 11, 26)")
        self.FatorSeg.setGeometry(0, 0, 350.0, 40.0)
        self.FatorSeg.move(100.0, 220.0)

        self.CalcNPtsBtn = QPushButton("Calcular raio e diâmetro", self.ScrewCalcW10)
        self.CalcNPtsBtn.setFont(QFont("Arial", 20, 8, True))
        self.CalcNPtsBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.CalcNPtsBtn.move(100.0, 280.0)
        self.CalcNPtsBtn.clicked.connect(self.CalcNPts)
        
        self.Info = QLabel("Atenção: Se usar Força em N use Tensão em MPa \n Se usar Força em Kgf use Tensão em Kgf", self.ScrewCalcW10)
        self.Info.setFont(QFont("Arial", 16, 8, True))
        self.Info.setStyleSheet("color: rgb(17, 11, 26)")
        self.Info.move(15.0, 520.0)

    def CalcNPts (self):

        self.Input14 = self.Tensao.text()
        self.TensaoVar = float(self.Input14)
        self.Input15 = self.ForcaMPKg.text()
        self.ForcaVar = float(self.Input15)
        self.Input16 = self.Pontos.text()
        self.PontosVar = float(self.Input16)
        self.Input17 = self.FatorSeg.text()
        self.FatorSegVar = float(self.Input17)

        self.RespNPts0 = self.TensaoVar / self.FatorSegVar
        self.RespNPts1 = self.RespNPts0 * self.PontosVar * 3.14159265359
        self.RespNPts2 = (self.ForcaVar / self.RespNPts1) ** (1/2)
        self.RespNPts3 = self.RespNPts2 * 2

        self.RespNPtsLabel = QLabel(self.ScrewCalcW10)
        self.RespNPtsLabel.setText(str(self.RespNPts2))
        self.RespNPtsLabel.setFont(QFont("Arial", 20, 8, True))
        self.RespNPtsLabel.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespNPtsLabel.move(100.0, 340.0)
        self.RespNPtsLabel.show()

        self.RespNPtsLabel2 = QLabel("[mm], e diâmetro =", self.ScrewCalcW10)
        self.RespNPtsLabel2.setFont(QFont("Arial", 20, 8, True))
        self.RespNPtsLabel2.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespNPtsLabel2.move(100.0, 400.0)
        self.RespNPtsLabel2.show()

        self.RespNPtsLabel3 = QLabel(self.ScrewCalcW10)
        self.RespNPtsLabel3.setText(str(self.RespNPts3))
        self.RespNPtsLabel3.setFont(QFont("Arial", 20, 8, True))
        self.RespNPtsLabel3.setStyleSheet("color: rgb(17, 11, 26)")
        self.RespNPtsLabel3.move(100.0, 460.0)
        self.RespNPtsLabel3.show()
        

    def ScrewCalc11 (self):

        self.ScrewCalcW11 = QWidget()
        self.ScrewCalcW11.setGeometry(550, 180, 500, 640)
        self.ScrewCalcW11.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewCalcW11.setWindowTitle("força suportável por n parafusos")
        self.ScrewCalcW11.show()



#########################RoscaWindow########################################

    def CreateRosca (self):

        self.RoscaWindow = QWidget()
        self.RoscaWindow.setGeometry(150, 150, 1280, 650)
        self.RoscaWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.RoscaWindow.setWindowTitle("Seção das Roscas")
        self.RoscaWindow.setWindowIcon(QIcon("roscaIcon"))
        #space for function calls
        self.RoscaSceneandView()

        self.RoscaWindow.show()

    def RoscaSceneandView (self):

        self.RScene = QGraphicsScene(self.RoscaWindow)
        #pixmap prep

        self.RPix1 = QGraphicsPixmapItem(QPixmap("ScrewTW"))
        self.RPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.RPix1.setScale(1.1)

        #pix add

        self.RScene.addItem(self.RPix1)

        #view def
        def RScanVi (self):

            self.RView = QGraphicsView(self.RScene, self.RoscaWindow)
            self.RView.setGeometry(0, 0, 500, 650)

        RScanVi(self)


#########################MolaWindow########################################

    def CreateMolaW (self):

        self.molaWindow = QWidget()
        self.molaWindow.setGeometry(150, 150, 1280, 650)
        self.molaWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.molaWindow.setWindowTitle("Seção das Molas")
        self.molaWindow.setWindowIcon(QIcon("MolaIcon"))
        self.testeeeee2 = QLabel("teste2", self.molaWindow)
        #space for function calls
        self.MoSceneandView()

        self.molaWindow.show()

    def MoSceneandView (self):

        self.MolaScene = QGraphicsScene(self.molaWindow)
        #pixmap prep

        self.MPix1 = QGraphicsPixmapItem(QPixmap("molaW"))
        self.MPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.MPix1.setScale(0.60)

        #pix add

        self.MolaScene.addItem(self.MPix1)

        #view def
        def MolView (self):

            MolaView = QGraphicsView(self.MolaScene, self.molaWindow)
            MolaView.setGeometry(0, 0, 500, 650)

        MolView(self)


#########################PorcasWindow########################################

    def CreatePorcas (self):

        self.PorcasWindow = QWidget()
        self.PorcasWindow.setGeometry(150, 150, 1280, 650)
        self.PorcasWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.PorcasWindow.setWindowTitle("Seção das Porcas")
        self.PorcasWindow.setWindowIcon(QIcon("PorcasIcon"))
        self.testeeeee2 = QLabel("teste2", self.PorcasWindow)
        #space for function calls
        self.PorScanView()

        self.PorcasWindow.show()

    def PorScanView (self):

        self.Porscene = QGraphicsScene(self.PorcasWindow)
        #pixmap prep

        self.PorPix = QGraphicsPixmapItem(QPixmap("porcaW"))
        self.PorPix.setFlag(QGraphicsItem.ItemIsMovable)
        self.PorPix.setScale(0.5)

        #pix add

        self.Porscene.addItem(self.PorPix)

        #view def
        def PorcView (self):

            self.PorcaViewVar = QGraphicsView(self.Porscene, self.PorcasWindow)
            self.PorcaViewVar.setGeometry(0, 0, 500, 650)

        PorcView(self)


#########################EixoWindow########################################

    def CreateEixo (self):

        self.EixoWindow = QWidget()
        self.EixoWindow.setGeometry(150, 150, 1280, 650)
        self.EixoWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.EixoWindow.setWindowTitle("Seção dos Eixos")
        self.EixoWindow.setWindowIcon(QIcon("roscaIcon"))
        #space for function calls
        self.EixoSceneandView()

        self.EixoWindow.show()

    def EixoSceneandView (self):

        self.EixoScene = QGraphicsScene(self.EixoWindow)
        #pixmap prep

        self.EixoPix = QGraphicsPixmapItem(QPixmap("eixoW"))
        self.EixoPix.setFlag(QGraphicsItem.ItemIsMovable)
        self.EixoPix.setScale(1.6)

        #pix add

        self.EixoScene.addItem(self.EixoPix)

        #view def
        def EixoViewf (self):

            self.EixoView = QGraphicsView(self.EixoScene, self.EixoWindow)
            self.EixoView.setGeometry(0, 0, 500, 650)

        EixoViewf(self)


#########################ChaveWindow########################################

    def CreateChave (self):

        self.ChaveWindow = QWidget()
        self.ChaveWindow.setGeometry(150, 150, 1280, 650)
        self.ChaveWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ChaveWindow.setWindowTitle("Seção das Chavetas")
        self.ChaveWindow.setWindowIcon(QIcon("chavetaIcon"))
        #space for function calls
        self.ChaveSceneanView()

        self.ChaveWindow.show()

    def ChaveSceneanView (self):

        self.ChaveScene = QGraphicsScene(self.ChaveWindow)

        self.ChavePix = QGraphicsPixmapItem(QPixmap("chavetaW"))
        self.ChavePix.setFlag(QGraphicsItem.ItemIsMovable)
        self.ChavePix.setScale(0.6)

        self.ChaveScene.addItem(self.ChavePix)

        def ChaveView (self):

            self.ChaveViewf = QGraphicsView(self.ChaveScene, self.ChaveWindow)
            self.ChaveViewf.setGeometry(0, 0, 500, 650)

        ChaveViewf(self)

#########################SoldaWindow########################################

    def CreateSolda (self):

        self.SoldaWindow = QWidget()
        self.SoldaWindow.setGeometry(150, 150, 1280, 650)
        self.SoldaWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.SoldaWindow.setWindowTitle("Seção da Solda")
        self.SoldaWindow.setWindowIcon(QIcon("SoldaIcon"))
        #space for function calls
        self.SoldaSceneandView()

        self.SoldaWindow.show()

    def SoldaSceneandView (self):

        self.SoldaScene = QGraphicsScene(self.SoldaWindow)

        self.SoldaPix1 = QGraphicsPixmapItem(QPixmap("SoldaW"))
        self.SoldaPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.SoldaPix1.setScale(0.8)

        self.SoldaScene.addItem(self.SoldaPix1)

        def SoldaView (self):

            self.SoldaViewf = QGraphicsView(self.SoldaScene, self.SoldaWindow)
            self.SoldaViewf.setGeometry(0, 0, 500, 650)

        SoldaView(self)


#########################MancaisWindow########################################

    def CreateMancais (self):

        self.MancaisWindow = QWidget()
        self.MancaisWindow.setGeometry(150, 150, 1280, 650)
        self.MancaisWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.MancaisWindow.setWindowTitle("Seção dos Mancais")
        self.MancaisWindow.setWindowIcon(QIcon("mancalIcon"))
        #space for function calls
        self.MancaisScanView()

        self.MancaisWindow.show()

    def MancaisScanView (self):

        self.MancalScene = QGraphicsScene(self.MancaisWindow)

        self.MancalPix1 = QGraphicsPixmapItem(QPixmap("mancalW"))
        self.MancalPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.MancalPix1.setScale(1.5)

        self.MancalScene.addItem(self.MancalPix1)

        def MancalView (self):

            self.MancView = QGraphicsView(self.MancalScene, self.MancaisWindow)
            self.MancView.setGeometry(0, 0, 500, 650)

        MancalView(self)


#########################CaboWindow########################################

    def CreateCabo (self):

        self.CaboWindow = QWidget()
        self.CaboWindow.setGeometry(150, 150, 1280, 650)
        self.CaboWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.CaboWindow.setWindowTitle("Seção dos Cabos")
        self.CaboWindow.setWindowIcon(QIcon("CaboAlma"))
        #space for function calls
        self.CaboScnandView()

        self.CaboWindow.show()

    def CaboScnandView (self):

        self.CaboScene = QGraphicsScene(self.CaboWindow)

        self.CaboPix1 = QGraphicsPixmapItem(QPixmap("caboW"))
        self.CaboPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.CaboPix1.setScale(1.6)

        self.CaboScene.addItem(self.CaboPix1)

        def CaboViewF (self):

            self.CaboView = QGraphicsView(self.CaboScene, self.CaboWindow)
            self.CaboView.setGeometry(0, 0, 500, 650)

        CaboViewF(self)




 
############################Ending###########################################


if __name__ == "__main__":
    app = QApplication([])
    janela = MainWindow()
    sys.exit(app.exec())