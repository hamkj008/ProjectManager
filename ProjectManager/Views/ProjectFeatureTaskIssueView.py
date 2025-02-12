from icecream import ic

from PySide6.QtWidgets import QWidget

from UiViews.UiProjectFeatureTaskIssueWindow import Ui_ProjectFeatureTaskIssueWindow
from Views.FeatureTabView import FeatureTabView
from Views.TaskTabView import TaskTabView
from Views.IssueTabView import IssueTabView
from MyHelperLibrary.Helpers.ResizableGrid import Direction, ResizeableGrid


# ========================================================================================
      

class ProjectFeatureTaskIssueView(QWidget):
    
    def __init__(self, viewController, search=None, currentIndex=0):
        super().__init__()
        
        self.viewController = viewController
        self.searchText     = search 
        self.currentIndex   = currentIndex

        self.editing        = False
        self.viewList       = {}

        # ----- Setup UI ------
        self.window = Ui_ProjectFeatureTaskIssueWindow()
        self.window.setupUi(self)
        self.setStyle()
        # ---------------------
       
        dividers = [(self.window.ProjectTabFrame, self.window.DescriptionFrame)]
        resizeableGrid = ResizeableGrid(dividers=dividers, direction=Direction.VERTICAL)

        self.window.BottomFrame.layout().addWidget(resizeableGrid)

        resizeableGrid.layout().addWidget(self.window.ProjectTabFrame, 0, 0)
        resizeableGrid.layout().addWidget(self.window.DescriptionFrame, 1, 0)
        resizeableGrid.layout().setVerticalSpacing(10)
        self.window.ProjectTabFrame.setParent(resizeableGrid)
        self.window.DescriptionFrame.setParent(resizeableGrid)

        # -- Signals ----
        self.window.tabWidget.setCurrentIndex(self.currentIndex)
        self.window.tabWidget.currentChanged.connect(self.tabChanged)
        self.window.BackBtn.clicked.connect(self.goBack) 
        self.window.AddNewBtn.clicked.connect(self.addNew)
        self.viewController.statusBar().showMessage("")
        

        self.getProjectName()       
           
        # Create the child tab views
        self.createFeatureTabView()
        self.createTaskTabView()
        self.createIssueTabView()


        self.tabChanged(self.currentIndex)


    # ========================================================================================
    

    def setStyle(self):

        styleSheet = self.viewController.qssController.getStandardStyle()
        styleSheet += self.viewController.qssController.getProjectFeatureTaskIssueStyle()
        self.setStyleSheet(styleSheet)


    # ========================================================================================
    

    def loadSelf(self):

        self.setActiveWindow(self.currentIndex)
    

    # # ========================================================================================
    

    def setActiveWindow(self, index):
            
        if index    == 0:
            self.viewList["featureView"].loadSelf()
            
        elif index  == 1:
            self.viewList["taskView"].loadSelf()
            
        elif index  == 2:
            self.viewList["issueView"].loadSelf()
     
            
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
    


    
