from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from widgets.centralwidget.ui.welcome import Ui_Form


class WelcomePage(QWidget, Ui_Form):
    def __init__(self):
        super(WelcomePage,self).__init__()
        #uic.loadUi(r'widgets\centralwidget\ui\welcome.ui', self)
        self.setupUi(self)
        self.setStyleSheet("color: #ffffff; border:0px; padding:50px; padding-bottom: 0px;" )
        logo = QPixmap(":resources/logo.png")
        self.labelLogo.setStyleSheet("padding:0px;")
        self.labelLogo.setPixmap(logo.scaled(200,200, Qt.KeepAspectRatio))
        
