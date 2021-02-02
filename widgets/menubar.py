from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QMessageBox, QHBoxLayout, 
                             QAction, QLabel, QMenuBar, QAction,  QListWidget,
                             QStyleFactory)
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtCore import Qt,QFile,QTextStream, QDir,QFileInfo
# ToolBar
class MenuBar(QMenuBar):

    def __init__(self):
        super().__init__()
        
        self.currentFile = "No opened files found"
        
        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)
        
      

        
        

        
        self.init_ui()
        

    def init_ui(self):
        
        self.fileMenu = self.addMenu("File")
        
        
                
        self.plotMenu = self.addMenu("Plot")
        

        self.helpMenu = self.addMenu("Help")
        self.helpMenu.addAction(self.aboutAct)
    
    def about(self):
        QMessageBox.about(self, "About Application",
            """  <h1>Genetic Plotter</h1>This application has comfortable\r
and friendly (easy-to-use) graphical user interface.\n
Genetic Plotter allows to conduct some types of\n
genetic data analysis and to visualize the result.""")


        

