from PyQt5.QtCore import QThread
from core.plotsettings import PlotSettings
from core.calc import GenConst
from core.xydata import XYdata


class CalculationalThread(QThread):
    def __init__(self,xydata, plotsettings):
        super(CalculationalThread, self).__init__()
        self.xydata = xydata
        self.plotsettings = plotsettings
        

    def run(self):
        self.plotsettings.setXYdataList(self.xydata.getXYdataList())




class Model:

    def __init__(self):

        self.file = "AL.txt"
        self.plotsettings = PlotSettings()
        self.xydata = XYdata()
        self.calc_thread = CalculationalThread(self.xydata, self.plotsettings)

        

    def setFile(self, file):
        self.file = file


    def run_xy_thread(self):
        
        self.xydata.setFileName(self.file)
        self.xydata.setPointsCount(self.plotsettings.getPointsCount())
        self.xydata.setSubseqList(self.plotsettings.getSubseqList())

        self.calc_thread.start()

        

        

