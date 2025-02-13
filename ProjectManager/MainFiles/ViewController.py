from icecream import ic
from PySide6.QtWidgets import QWidget, QStatusBar
from PySide6.QtCore import Qt

from UiViews.UiMainWidget import Ui_MainWidget
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
from Views.PreferencesView import PreferencesView

from MyHelperLibrary.Helpers.CustomWindow import CustomWindow
from MyHelperLibrary.Helpers.HelperMethods import clearStackedLayout

# ========================================================================================
      

class ViewController(CustomWindow):

    
    def __init__(self, main):

        iconPath = "E:/MyITstuff/ProgrammingIDEs/VisualStudio/Python/Projects/ProjectManager/ProjectManager/icons/ProjectManagerIcon.png"        # have to pass an absolute path
        super().__init__("Project Manager", iconPath, True)
        # ----------------------
        
        self.Main               = main
        
        self.stateController    = StateController()
        self.qssController      = QSSController()
        self.menuController     = MenuController(self)
       
        self.modelCreator       = ModelCreator(databaseName='projectManager.db')
        self.model              = ProjectModel(self.modelCreator.connection)
        
        self.viewList           = {}
        self.menuList           = {}  


        # ----- Setup UI ----------------
        self.container  = QWidget()
        self.content    = Ui_MainWidget()
        self.content.setupUi(self.container)
        
        self.setCentralWidget(self.container)
        self.setStyle()
        # -------------------------------  

        self.setMinimumSize(300, 200)

        # -- Menu bar --
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
        methodName  = f"display{viewToDisplay}"
        
        # Use getattr to get the appropriate method
        method      = getattr(self, methodName, None)
        
        newWindow   = kwargs.pop('newWindow', False)
        
        if method and callable(method):
            if not newWindow:
                clearStackedLayout(self.viewList, self.content.stackedWidget)        # Clear the layout

            method(*args, **kwargs)                                                 # display the view 
            # self.menuController.refreshContextMenus()       # refresh the menus for correct context
            
        else:
            ic(f"No method found for display{viewToDisplay}")
         
            
    # ========================================================================================
    
    
    def closeView(self, viewToDisplay):
        
        # Construct the method name
        methodName  = f"close{viewToDisplay}"
        
        # Use getattr to get the appropriate method
        method      = getattr(self, methodName, None)
        
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
        self.content.stackedWidget.addWidget(self.viewList["projectView"])
        self.content.stackedWidget.setCurrentWidget(self.viewList["projectView"])
        ic(self.content.stackedWidget.layout().count())

    # ========================================================================================
    
    
    def displayProjectFeatureTaskIssueView(self, search=None, currentIndex=0):
        ic("displayProjectFeatureTaskIssueView")

        self.viewList["projectFeatureTaskIssueView"] = ProjectFeatureTaskIssueView(self, search, currentIndex)
        self.content.stackedWidget.addWidget(self.viewList["projectFeatureTaskIssueView"])
        self.content.stackedWidget.setCurrentWidget(self.viewList["projectFeatureTaskIssueView"])
     
        
    # ========================================================================================
     
    def displayPreferencesView(self):
        self.viewList["preferencesView"] = PreferencesView(self, self.qssController)
        self.viewList["preferencesView"].main()
    
    def closePreferencesView(self):
        self.viewList["preferencesView"].close()
        
        
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
        
