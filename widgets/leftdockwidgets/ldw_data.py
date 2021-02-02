from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


from widgets.leftdockwidgets.ui.data_dockwidget import Ui_mainWidget

class LeftDockWidgetData(QWidget,Ui_mainWidget):
    def __init__(self):
        super(LeftDockWidgetData,self).__init__()
        #uic.loadUi(r'widgets\leftdockwidgets\ui\data_dockwidget.ui', self)
        self.setupUi(self)
        
        
