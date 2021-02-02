from PyQt5.QtWidgets import QListWidgetItem
import time

class CoreController:    

    def __init__(self,pself):
        self.projectmodel = pself

    def modelPlotSettingsUpdate(self):
        self.projectmodel.model.plotsettings.setSubseqList(self.projectmodel.ldw.plot.getSubseqList())
        self.projectmodel.model.plotsettings.setColorsList(self.projectmodel.ldw.plot.getColorsList())
        self.projectmodel.model.plotsettings.setPointsCount(self.projectmodel.ldw.plot.getPointsCount())
        
        self.projectmodel.model.setFile(self.projectmodel.ldw.main.getFilePath())
        # must apply only after plotsettings.setSubseqList()
        self.projectmodel.model.run_xy_thread()
