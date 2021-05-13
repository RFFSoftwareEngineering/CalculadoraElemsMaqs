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


#########################################################################testegitiniciando coding
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
            self.tituloani.setPosAt(0.9, QPointF(-1100, 0))
            self.tituloani.setPosAt(1, QPointF(-1600, 0))

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
        self.GearsBtn.move(515, 140)
        self.GearsBtn.clicked.connect(self.CreateNewWin)
        self.ParafBtn = QPushButton("Cálculo de Parafusos", self)
        self.ParafBtn.setFont(QFont("Arial", 20, 8, True))
        self.ParafBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.ParafBtn.setIcon(QIcon("ParafusoIcon"))
        self.ParafBtn.move(915, 140)
        self.RebitBtn = QPushButton("Cálculo de Rebites", self)
        self.RebitBtn.setFont(QFont("Arial", 20, 8 , True))
        self.RebitBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.RebitBtn.setIcon(QIcon("RebiteIcon"))
        self.RebitBtn.move(525, 240)
        self.MolasBtn = QPushButton("Cálculo de Molas", self)
        self.MolasBtn.setFont(QFont("Arial", 20, 8, True))
        self.MolasBtn.setStyleSheet("color: rgb(17 ,11, 26)")
        self.MolasBtn.setIcon(QIcon("MolaIcon"))
        self.MolasBtn.move(915, 240)
        self.EixoBtn = QPushButton("Cálculo de Eixos", self)
        self.EixoBtn.setFont(QFont("Arial", 20, 8, True))
        self.EixoBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.EixoBtn.setIcon(QIcon("eixoIcon"))
        self.EixoBtn.move(520, 340)
        self.SoldaBtn = QPushButton("Cálculo de Solda", self)
        self.SoldaBtn.setFont(QFont("Arial", 20, 8, True))
        self.SoldaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.SoldaBtn.setIcon(QIcon("SoldaIcon"))
        self.SoldaBtn.move(915, 340)
        self.PorcasBtn = QPushButton("Cálculo de Porcas", self)
        self.PorcasBtn.setFont(QFont("Arial", 20, 8, True))
        self.PorcasBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.PorcasBtn.setIcon(QIcon("PorcasIcon"))
        self.PorcasBtn.move(520, 440)
        self.MancaisBtn = QPushButton("Cálculo de Mancais", self)
        self.MancaisBtn.setFont(QFont("Arial", 20, 8, True))
        self.MancaisBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.MancaisBtn.setIcon(QIcon("mancalIcon"))
        self.MancaisBtn.move(915, 440)
        self.CaboBtn = QPushButton("Cálculo de Cabos de Aço", self)
        self.CaboBtn.setFont(QFont("Arial", 20, 8, True))
        self.CaboBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.CaboBtn.setIcon(QIcon("CaboAlma"))
        self.CaboBtn.move(515, 540)
        self.ChaveBtn = QPushButton("Cálculo de Chavetas", self)
        self.ChaveBtn.setFont(QFont("Arial", 20, 8, True))
        self.ChaveBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.ChaveBtn.setIcon(QIcon("chavetaIcon"))
        self.ChaveBtn.move(920, 540)
        self.RoscaBtn = QPushButton("Cálculo de Roscas", self)
        self.RoscaBtn.setFont(QFont("Arial", 20, 8, True))
        self.RoscaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.RoscaBtn.setIcon(QIcon("roscaIcon"))
        self.RoscaBtn.move(720, 640)
        

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

        #pix add:
        self.SceneGears.addItem(self.GPix1)
        self.SceneGears.addItem(self.G2Pix)
        self.SceneGears.addItem(self.g3Pix)
        self.SceneGears.addItem(self.g5pix)

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
        self.lineGears.setLoopCount(0)

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
            self.g3anim.setPosAt(0.094,QPointF(-1200, 0))

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

        #animations finalization:
        GAnime1(self)
        GA2nime(self)
        G3Ani(self)
        G4Ani(self)
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
        self.ResultadoField.move(75, 80)
        self.ResultadoField.show()
        
    def testLabel (self):

        self.testeeeee = QLabel("teste", self.Windowisidewindow)
        

        
        
 
############################Ending###########################################

if __name__ == "__main__":
    app = QApplication([])
    janela = MainWindow()
    sys.exit(app.exec_())