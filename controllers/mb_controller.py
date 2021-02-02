from PyQt5.QtWidgets import QAction
class MbController:    #menu bar controller

    def __init__(self,pself):
        self.genplotter = pself
        self.init_mb_actions()
        self.genplotter.mb.fileMenu.addAction(self.genplotter.mb.open_file)
        self.genplotter.mb.plotMenu.addAction(self.genplotter.mb.save_png)
        self.genplotter.mb.plotMenu.addAction(self.genplotter.mb.save_jpg)


   
    def init_mb_actions(self):
        self.genplotter.mb.open_file = QAction("Open file", self.genplotter.mb,
                statusTip="Show the application's About box",
                triggered=self.genplotter.ldw.main.addFile)

        self.genplotter.mb.save_png = QAction("Save plot as PNG", self.genplotter.mb,
                triggered=self.genplotter.chartfield.save_png)

        self.genplotter.mb.save_jpg = QAction("Save plot as JPG", self.genplotter.mb,
                triggered=self.genplotter.chartfield.save_jpg)

        