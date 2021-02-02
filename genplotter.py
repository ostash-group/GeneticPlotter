from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

from projectmodel import ProjectModel 
from widgets.centralwidget.chartfield import ChartField
from widgets.mainwindow import MainWindow

from controllers.ldw_controller import LdwController
from controllers.tb_controller import TbController
from controllers.mb_controller import MbController


class GenPlotter():
    
    def __init__(self):
        super().__init__() # mb tb ldw are included
        self.pm = ProjectModel()
        self.pm.mw = MainWindow()
        self.pm.chartfield = ChartField()

        self.pm.c1 = LdwController(self.pm)
        self.pm.c2 = TbController(self.pm)
        self.pm.c3 = MbController(self.pm)


        self.pm.mw.setMenuBar(self.pm.mb)
        self.pm.mw.addToolBar(Qt.LeftToolBarArea, self.pm.tb)
        self.pm.mw.addDockWidget(Qt.LeftDockWidgetArea,self.pm.ldw,Qt.Vertical)
        self.pm.mw.setCentralWidget(self.pm.chartfield)
        self.pm.mw.showMaximized()

