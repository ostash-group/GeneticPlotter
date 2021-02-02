from PyQt5.QtWidgets import QDockWidget

from widgets.leftdockwidgets.ldw_main import LeftDockWidgetMain
from widgets.leftdockwidgets.ldw_plot import LeftDockWidgetPlot
from widgets.leftdockwidgets.ldw_tools import LeftDockWidgetTools
from widgets.leftdockwidgets.ldw_data import LeftDockWidgetData

class LeftDockWidget(QDockWidget):

    def __init__(self):
        super().__init__()
        
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.main = LeftDockWidgetMain()
        self.plot = LeftDockWidgetPlot()
        self.tools = LeftDockWidgetTools()
        self.data = LeftDockWidgetData()
        self.setWidget(self.main)
