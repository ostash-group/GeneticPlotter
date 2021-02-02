

from widgets.leftdockwidgets.leftdockwidget import LeftDockWidget
from widgets.menubar import MenuBar
from widgets.toolbar import ToolBar
from core.model import Model
from core.xydata import XYdata
from controllers.core_controller import CoreController

class ProjectModel:

    def __init__(self):

        self.mb = MenuBar()
        self.tb = ToolBar()
        self.ldw = LeftDockWidget()
        self.data = XYdata()
        
        self.model = Model()
        self.core_controller = CoreController(self)
    
    