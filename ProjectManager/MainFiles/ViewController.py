from icecream import ic
from PySide6.QtWidgets import QMainWindow, QStatusBar
from PySide6.QtCore import Qt

from UiViews.UiMainWindow import Ui_MainWindow
from MainFiles.QSSController import QSSController
from MainFiles.StateController import StateController
from MainFiles.MenuController import MenuController

from Models.ProjectModel import ProjectModel
from Models.ModelCreator import ModelCreator

from Views.ProjectView import ProjectView
from Views.ProjectFeatureTaskIssueView import ProjectFeatureTaskIssueView
from Views.AboutView import AboutView
from Views.AddNewProjectView import AddNewProjectView
from Views.AddNewView import AddNewView

from MyHelperLibrary.Helpers.HelperMethods import clearStackedLayout

# ========================================================================================
      

class ViewController(QMainWindow):

    
    def __init__(self, main, logController):
        super().__init__()

        self.Main = main
        self.logController = logController
        
        self.stateController = StateController()
        self.qssController = QSSController()
        self.menuController = MenuController(self)
       
        self.modelCreator = ModelCreator()
        self.model = ProjectModel(self.modelCreator.connection)
        
        self.viewList = {}
        self.menuList = {}


        # --- Setup UI ---
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.setWindowTitle("Project Manager")
        self.setStyle()
        # -------------------------------    

        # -- Menu bar --
        self.menubar = self.menuBar()
        self.menuController.setupMenus(self.menubar)
        
        # -- Status bar --
        self.setStatusBar(QStatusBar(self))  
        
        # -- Start --
        self.displayView("ProjectView")

    # ========================================================================================
        

    def main(self):        
        self.show()


    # ========================================================================================


    def setStyle(self):
        ic("setStyle")
        
        self.setStyleSheet(self.qssController.getStandardStyle())
        
        for view in self.viewList.values():
            if view:
                view.setStyle()
                if hasattr(view, "loadSelf"):
                    view.loadSelf()


    # ========================================================================================


    """Dynamically calls a method to display a view.    
    @viewToDisplay: The name of the view to display (e.g., 'PreferencesView').
    @args: Positional arguments to pass to the display method.
    @kwargs: Keyword arguments to pass to the display method."""
    
    def displayView(self, viewToDisplay, *args, **kwargs):
        
        # Construct the method name
        methodName = f"display{viewToDisplay}"
        
        # Use getattr to get the appropriate method
        method = getattr(self, methodName, None)
        
        newWindow = kwargs.pop('newWindow', False)
        
        if method and callable(method):
            if not newWindow:
                clearStackedLayout(self.viewList, self.window.stackedWidget)        # Clear the layout

            method(*args, **kwargs)                                                 # display the view 
            # self.menuController.refreshContextMenus()       # refresh the menus for correct context
            
        else:
            ic(f"No method found for display{viewToDisplay}")
         
            
    # ========================================================================================
    
    
    def closeView(self, viewToDisplay):
        
        # Construct the method name
        methodName = f"close{viewToDisplay}"
        
        # Use getattr to get the appropriate method
        method = getattr(self, methodName, None)
        
        if method and callable(method):
            method()                                   # display the view
        
        else:
            ic(f"No method found for close{viewToDisplay}")
            

    # ========================================================================================
    

    def displayAboutView(self):
        
        versionNumber = self.stateController.getVersionNumber()
        self.viewList["aboutView"] = AboutView(self, versionNumber)
        self.viewList["aboutView"].main()
    
    def closeAboutView(self):
        self.viewList["aboutView"].close()
        

    # ========================================================================================
    

    def displayProjectView(self):
        ic("displayProjectView")
        
        self.viewList["projectView"] = ProjectView(self)
        self.window.stackedWidget.addWidget(self.viewList["projectView"])
        self.window.stackedWidget.setCurrentWidget(self.viewList["projectView"])
        

    # ========================================================================================
    
    
    def displayProjectFeatureTaskIssueView(self, search=None, currentIndex=0):
        ic("displayProjectFeatureTaskIssueView")

        self.viewList["projectFeatureTaskIssueView"] = ProjectFeatureTaskIssueView(self, search, currentIndex)
        self.window.stackedWidget.addWidget(self.viewList["projectFeatureTaskIssueView"])
        self.window.stackedWidget.setCurrentWidget(self.viewList["projectFeatureTaskIssueView"])
     
        
    # ========================================================================================
    

    def displayAddNewProjectView(self, projectDict=None, editing=False):
        self.viewList["addNewProjectView"] = AddNewProjectView(self, projectDict, editing)
        self.viewList["addNewProjectView"].main()
    
    def closeAddNewProjectView(self):
        self.viewList["addNewProjectView"].close()
        
        
    # ========================================================================================
    
    
    def displayAddNewView(self, parentView, index, objectDict=None, editing=False):
        self.viewList["addNewView"] = AddNewView(self, parentView, index, objectDict, editing)
        self.viewList["addNewView"].main()

    
    def closeAddNewView(self):
        self.viewList["addNewView"].close()


    # ========================================================================================
    

    def closeDatabase(self):
            
        self.model.connection.close()
        self.modelCreator.connection.close()
    

    # ========================================================================================
    
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.Main.exit()
        
