from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


from widgets.leftdockwidgets.ui.tools_dockwidget import Ui_mainWidget


class LeftDockWidgetTools(QWidget,Ui_mainWidget):
    def __init__(self):
        super(LeftDockWidgetTools,self).__init__()
        #uic.loadUi(r'widgets\leftdockwidgets\ui\tools_dockwidget.ui', self)
        self.setupUi(self)

        self.labelDesc.setWordWrap(True)
        self.labelDesc.setStyleSheet("padding: 5px;")
        self.labelDesc.setFixedWidth(254)
