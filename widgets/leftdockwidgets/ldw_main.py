from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel, QTableWidgetItem, QComboBox
from PyQt5.QtCore import QUrl,QFileInfo
from widgets.leftdockwidgets.ldw_plot import ImgWidgetDel

from widgets.leftdockwidgets.ui.main_dockwidget import Ui_mainWidget
import resources
class LeftDockWidgetMain(QWidget,Ui_mainWidget):
    def __init__(self):
        super(LeftDockWidgetMain,self).__init__()
        #uic.loadUi(r'widgets\leftdockwidgets\ui\main_dockwidget.ui', self)
        self.setupUi(self)
        

        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 50)
        self.table.setColumnWidth(2, 70)
        self.table.setColumnWidth(3, 20)
        self.table.setColumnWidth(4, 1)

 
        self.addButton.clicked.connect(self.addFile)
        self.table.cellClicked.connect(self.cellWasClicked)



        #setItemText(int index, const QString &text) setMaxVisibleItems(int maxItems)
        #addItems(const QStringList &texts) removeItem(int index)


    def addFile(self):


        fileInfo = QFileInfo(QFileDialog.getOpenFileName(self)[0])
        if(not fileInfo.isFile()): return 0
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        
        self.table.setCellWidget(rowPosition , 0, QLabel(fileInfo.fileName()))
        self.table.setCellWidget(rowPosition , 1, QLabel(str(round(int(fileInfo.size())/(1024*1024),3))+"Mb"))
        self.table.setCellWidget(rowPosition , 2, QLabel(
            str(self.get_genes_count(str(fileInfo.absoluteFilePath())))+" genes"))
        self.table.setCellWidget(rowPosition,3,ImgWidgetDel(":resources/close.png"))
        
        self.table.setItem(rowPosition , 4, QTableWidgetItem(fileInfo.absoluteFilePath()))

        self.comboBox.addItem(fileInfo.fileName())
        #comboBox



    def cellWasClicked(self, row, column):
        if (column==3):
            self.table.removeRow(row)
            self.comboBox.removeItem(row)


    def getFilePath(self):
        t_item = self.table.item(self.comboBox.currentIndex(),4)
        print(self.comboBox.currentIndex())
        return(t_item.text())

        
    def get_genes_count(self,path):
        '''read genome file from my disk'''
        genes_count = 0
        f = open(path,'r')
        for line in f:
            if line.startswith('>lcl'):
                genes_count+=1
                
        f.close()
        return(genes_count)