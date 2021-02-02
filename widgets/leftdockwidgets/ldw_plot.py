import random
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QLabel, QColorDialog
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor, QImage
from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex, QDir, QSize
from widgets.leftdockwidgets.ui.plot_dockwidget import Ui_mainWidget
import resources

START_POINTS_COUNT=50


class ImgWidget(QLabel):

    def __init__(self, path, color):
        super(ImgWidget, self).__init__()
        icon = QIcon(path)
        pic = icon.pixmap(QSize(20, 20))
        self.setPixmap(pic)
        self.setStyleSheet("background-color: %s; 	width: 20px; height: 20px;" %
            color.name())

class ImgWidgetDel(QLabel):

    def __init__(self, path):
        super(ImgWidgetDel, self).__init__()
        icon = QIcon(path)
        pic = icon.pixmap(QSize(16, 16))
        self.setPixmap(pic)
        self.setStyleSheet("width: 20px; height: 20px; padding:1;")


class LeftDockWidgetPlot(QWidget,Ui_mainWidget):
    def __init__(self):
        super(LeftDockWidgetPlot,self).__init__()
        
        #uic.loadUi(r'widgets\leftdockwidgets\ui\plot_dockwidget.ui', self)
        self.setupUi(self)
        self.table.setColumnWidth(1, 20)
        self.table.setColumnWidth(2, 20)
        

        self.colors = ["#ff0000","#00aa00","#0000ff","#ff00ff","#aaaa7f","#00ff00","#aa5500",
        "#ffaa00","#808000","#008080","#800080","#800000"]
        self.color_ind=0

        self.spinBox.setValue(START_POINTS_COUNT)
        self.pointsSlider.setValue(START_POINTS_COUNT)

        self.pointsSlider.sliderMoved.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.pointsSlider.setValue)


        self.table.cellClicked.connect(self.cellWasClicked)
        self.addButton.clicked.connect(self.pushSubseqToTable)

        
        

    def addTableItem(self,str):
        
        #random color
        color = QColor( self.colors[self.color_ind] )
        self.color_ind =  (self.color_ind+1) if (self.color_ind<len(self.colors)-1) else 0
        

        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setCellWidget(rowPosition , 0, QLabel(str))
        self.table.setCellWidget(rowPosition,1,ImgWidget(":resources/e_round.png",color))
        self.table.setCellWidget(rowPosition,2,ImgWidgetDel(":resources/close.png"))
        


    def cellWasClicked(self, row, column):
        if (column==1):
            color = QColorDialog.getColor()
            self.table.setCellWidget(row,1,ImgWidget(":resources/e_round.png",color))
        if (column==2):
            self.table.removeRow(row)
            
            

    def pushSubseqToTable(self):
        self.addTableItem(self.subseqEdit.text())
        self.subseqEdit.clear()



    def getSubseqList(self):
        self.subseq = []
        for row in range(self.table.rowCount()):
            t_item = self.table.cellWidget(row,0)
            self.subseq.append(t_item.text())
        return(self.subseq)


    def getColorsList(self):
        self.colors_list = []
        for row in range(self.table.rowCount()):
            w = self.table.cellWidget(row,1)
            color = w.palette().color(QPalette.Background)
            #print (color.red(), color.green(), color.blue())
            self.colors_list.append(color)
        return(self.colors_list)

    def getPointsCount(self):
        return(self.spinBox.value())

        


