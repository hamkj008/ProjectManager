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
from MyHelperLibrary.Helpers.HelperMethods import createDisplayView, createCloseView, getCurrentFunction
from MyHelperLibrary.LogController.Logger import setupLogger

# ========================================================================================

class ViewController(CustomWindow):

    def __init__(self, main, iconPath):
        super().__init__("Project Manager", iconPath, True)
        ic(__class__.__name__)
        # ----------------------
        
        setupLogger(self, "Project Manager")
        
        self.Main               = main
        self.viewList           = {}
        self.stateController    = StateController()
        self.qssController      = QSSController()
        self.menuController     = MenuController(self)
    
        self.modelCreator       = ModelCreator(databaseName='projectManager.db')
        self.model              = ProjectModel(self, self.modelCreator.connection)

        # ----- UI ----------------
        self.container  = QWidget()
        self.content    = Ui_MainWidget()
        self.content.setupUi(self.container)
        self.setCentralWidget(self.container)
        self.setStyle()
        self.setMinimumSize(300, 200)
        # -------------------------------  

        # ----- Setup ----------------
        self.displayView        = createDisplayView(self, self.content.stackedWidget, self.viewList)
        self.closeView          = createCloseView(self)
        
        self.menuController.setupMenus(self.menubar)    # menubar comes from the custom window
        self.setStatusBar(QStatusBar(self))  
        # -------------------------------  

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
    
    def displayAboutView(self):
        versionNumber = self.stateController.getVersionNumber()
        self.viewList["aboutView"] = AboutView(self, versionNumber)
        self.viewList["aboutView"].main()
    
    def closeAboutView(self):
        self.viewList["aboutView"].close()

    # ========================================================================================
    
    def displayProjectView(self):
        self.log(self.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        self.viewList["projectView"] = ProjectView(self)
        self.content.stackedWidget.addWidget(self.viewList["projectView"])
        self.content.stackedWidget.setCurrentWidget(self.viewList["projectView"])

    # ========================================================================================
    
    def displayProjectFeatureTaskIssueView(self, search=None, currentIndex=0):
        self.log(self.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

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
        
