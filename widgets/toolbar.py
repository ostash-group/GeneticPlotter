from PyQt5.QtWidgets import (QToolBar,QPushButton,QVBoxLayout,QWidget)
from PyQt5.QtCore import Qt



class ToolBarButtons(QPushButton):
    def __init__(self,str):
        super().__init__()
        self.setText(str)
        self.setCheckable(True)
        self.setChecked(False)


class ToolBar(QToolBar):

    def __init__(self):
        super().__init__()

        SPACING = 0 # Spacing = 0px

        self.setFloatable(False)
        self.setMovable(False)
        self.setContextMenuPolicy(Qt.NoContextMenu)

        
        
        # information about genome, also for adding genes
        self.main_b = ToolBarButtons("Main")

        # for choosing type of genetic analysis, adding subplots
        self.tools_b = ToolBarButtons("Tools")

        # plot options
        self.plot_b = ToolBarButtons("Plot")

        # import data in cvs or xlsx\xls files 
        self.data_b = ToolBarButtons("Data")

        vb = QVBoxLayout()
        
        vb.addWidget(self.main_b)
        vb.addWidget(self.tools_b)
        vb.addWidget(self.plot_b)
        vb.addWidget(self.data_b)
        vb.setSpacing(SPACING)
        vb.setContentsMargins(SPACING,SPACING,SPACING,SPACING)
        self.t_buttons = QWidget()
        self.t_buttons.setLayout(vb)
        self.addWidget(self.t_buttons)
        #self.addWidget(self.main_b)
        #self.addWidget(self.plot_b)
        #self.addWidget(self.genome_b)
        #self.addWidget(self.data_b)


