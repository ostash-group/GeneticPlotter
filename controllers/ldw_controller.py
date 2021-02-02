from PyQt5.QtWidgets import QListWidgetItem, QMessageBox

import time

class LdwController:    #left dock widget controller

    def __init__(self,pself):
        self.genplotter = pself


        self.genplotter.ldw.plot.createChartButton.clicked.connect(self.start_replot)
        self.genplotter.model.calc_thread.finished.connect(self.finish_replot)


        self.genplotter.ldw.plot.savePNGButton.clicked.connect(self.genplotter.chartfield.save_png)
        self.genplotter.ldw.plot.saveJPGButton.clicked.connect(self.genplotter.chartfield.save_jpg)


        

    def start_replot(self):

        if (self.genplotter.ldw.main.comboBox.currentIndex()== -1):
            msg = QMessageBox()
            msg.setWindowTitle("MessageBox")
            msg.setFixedWidth(500)
            msg.setIcon(QMessageBox.Information)
            msg.setText("You can`t make a chart now!")
            msg.setInformativeText("No opened files found. Click on File -> Open... in MenuBar and choose the file.")
            
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.exec_()
        else:
            self.genplotter.core_controller.modelPlotSettingsUpdate()
            self.genplotter.chartfield.spinnerView()
            self.genplotter.mw.setCentralWidget(self.genplotter.chartfield)
            self.genplotter.chartfield.setCurrentIndex(1)

    def finish_replot(self):
        xydata = self.genplotter.model.plotsettings.getXYdataList()
        colors = self.genplotter.model.plotsettings.getColorsList()
        subseqences = self.genplotter.model.plotsettings.getSubseqList()
        self.genplotter.chartfield.chart.removeAllSeries()

        max_value = 1
        for i in range(len(xydata)):
            max_value = max(xydata[i][1]) if  max(xydata[i][1]) >max_value else max_value


        axsis_label = [5,6,7.5,10,15,20,25,30,40]
        ax = []
        axsis = []
        for i in range(5):
            for j in range(len(axsis_label)):
                ax.append(axsis_label[j]*(10**i)*4)
            axsis.extend(ax)

        for i in axsis:
            if max_value< (i - 0.1*i): 
                max_value = i
                break


        for i in range(len(xydata)):
            self.genplotter.chartfield.add_data(xydata[i][0],xydata[i][1],colors[i],max_value,subseqences[i])
        self.genplotter.chartfield.chartView()
        self.genplotter.mw.setCentralWidget(self.genplotter.chartfield)




        