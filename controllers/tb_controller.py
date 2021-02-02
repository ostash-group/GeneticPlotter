
class TbController:    #tool bar controller

    def __init__(self,pself):
        self.genplotter = pself
        self.changeDockWidget()


    def changeDockWidget(self):

        self.genplotter.tb.main_b.clicked.connect(
            lambda :self.chekedButton(self.genplotter.tb.main_b))
        self.genplotter.tb.tools_b.clicked.connect(
            lambda :self.chekedButton(self.genplotter.tb.tools_b))
        self.genplotter.tb.plot_b.clicked.connect(
            lambda :self.chekedButton(self.genplotter.tb.plot_b))
        self.genplotter.tb.data_b.clicked.connect(
            lambda :self.chekedButton(self.genplotter.tb.data_b))


        self.genplotter.tb.main_b.clicked.connect(
            lambda : self.genplotter.ldw.setWidget(self.genplotter.ldw.main))
        self.genplotter.tb.tools_b.clicked.connect(
            lambda : self.genplotter.ldw.setWidget(self.genplotter.ldw.tools))
        self.genplotter.tb.plot_b.clicked.connect(
            lambda : self.genplotter.ldw.setWidget(self.genplotter.ldw.plot))
        self.genplotter.tb.data_b.clicked.connect(
            lambda : self.genplotter.ldw.setWidget(self.genplotter.ldw.data))

  
    def chekedButton(self,b):
        self.genplotter.tb.main_b.setChecked(False)
        self.genplotter.tb.tools_b.setChecked(False)
        self.genplotter.tb.plot_b.setChecked(False)
        self.genplotter.tb.data_b.setChecked(False)
        b.setChecked(True)
