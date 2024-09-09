from icecream import ic

from PySide6.QtWidgets import QWidget

from UiViews.UiProjectFeatureTaskIssueWindow import Ui_ProjectFeatureTaskIssueWindow
from Views.FeatureTabView import FeatureTabView
from Views.TaskTabView import TaskTabView
from Views.IssueTabView import IssueTabView
from MyHelperLibrary.Helpers.HelperMethods import clearLayout, removeClassFromLayout

# ========================================================================================
      

class ProjectFeatureTaskIssueView(QWidget):
    
    def __init__(self, viewController, search=None, currentIndex=0):
        super().__init__()
        
        self.viewController = viewController
        self.searchText = search 
        self.currentIndex = currentIndex


        # ----- Setup UI ------
        self.window = Ui_ProjectFeatureTaskIssueWindow()
        self.window.setupUi(self)
        self.setStyle()
        # ---------------------
        

        # -- Signals ----
        self.window.tabWidget.setCurrentIndex(self.currentIndex)
        self.window.tabWidget.currentChanged.connect(self.tabChanged)
        self.window.BackBtn.clicked.connect(self.goBack) 
        self.window.AddNewBtn.clicked.connect(self.addNew)
        self.viewController.statusBar().showMessage("")
        
        self.editing = False
        self.viewList = {}

        self.getProjectName()       
                
        self.tabChanged(self.currentIndex)


    # ========================================================================================
    

    def setStyle(self):
        
        styleSheet = self.viewController.qssController.getStandardStyle()
        styleSheet += self.viewController.qssController.getProjectFeatureTaskIssueStyle()
        self.setStyleSheet(styleSheet)


    # ========================================================================================
    
    
    def setActiveWindow(self, index):
        
        # Clear the views and layout so only one view will be active at a time
        for key in self.viewList.keys():
            self.viewList[key] = None
        
        # --------
            
        if index == 0:
            clearLayout(self.window.FeaturesTab.layout())  # From helpers
            self.createFeatureTabView()
            
        # TasksTab and IssueTab have child structures from the parent so can't just be wiped
        elif index == 1:
            if self.window.TasksTab.layout().count() > 1:
                # Remove all TaskTabViews from layout
                removeClassFromLayout(self.window.TasksTab.layout(), TaskTabView)  # From helpers
            self.createTaskTabView()
            
        elif index == 2:
            if self.window.IssuesTab.layout().count() > 1:
                # Remove all IssueTabViews from layout
                removeClassFromLayout(self.window.IssuesTab.layout(), IssueTabView)  # From helpers
            self.createIssueTabView()
     
            
        

    # ========================================================================================


    # -------- FEATURES TAB ----------------------------
    def createFeatureTabView(self):
        
        self.viewList["featureView"] = FeatureTabView(self, 0)
        self.window.FeaturesTab.layout().addWidget(self.viewList["featureView"]) 

    # -------- TASKS TAB ----------------------------
    def createTaskTabView(self):
        
        self.viewList["taskView"] = TaskTabView(self, 1)
        self.window.TasksTab.layout().addWidget(self.viewList["taskView"]) 


    # -------- ISSUES TAB ----------------------------
    def createIssueTabView(self):
        
        self.viewList["issueView"] = IssueTabView(self, 2)
        self.window.IssuesTab.layout().addWidget(self.viewList["issueView"]) 
        

    # ========================================================================================
    
    
    def getProjectName(self):
        
        projectName = self.viewController.model.getProjectName(self.viewController.stateController.projectId)
        self.window.TitleLabel.setText(projectName)
     

    # ========================================================================================


    def goBack(self):
        ic("goBack")
        
        self.viewController.displayView("ProjectView")
        

    # ======================================================================================== 
    
    
    def getPriorityDict(self):
        
        priorityDict = {0: {"Priority" : "Highest", "Color" : "red"},
                        1: {"Priority" : "High",    "Color" : "orange"},
                        2: {"Priority" : "Medium",  "Color" : "yellow"},
                        3: {"Priority" : "Low",     "Color" : "green"},
                        4: {"Priority" : "Lowest",  "Color" : "white"}}
        

        return priorityDict


    # ======================================================================================== 
    

    def tabChanged(self, index):
        ic("tabChanged")
        
        self.currentIndex = index
        self.setActiveWindow(index)
        self.window.DescriptionTextLabel.setText("")


    # ======================================================================================== 


    def addNew(self):
        ic("addNew")
        
        self.viewController.displayView("AddNewView", self, self.currentIndex, newWindow=True)
        
         
    # ========================================================================================
    


    
