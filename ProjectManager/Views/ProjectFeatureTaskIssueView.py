from icecream import ic
from UiViews.UiProjectFeatureTaskIssueWindow import Ui_ProjectFeatureTaskIssueWindow
from PySide6.QtWidgets import QWidget, QMenu, QPushButton, QSizePolicy
from PySide6.QtGui import QAction
from Views.FeatureTabView import FeatureTabView
from Views.TaskTabView import TaskTabView
from Views.IssueTabView import IssueTabView



class ProjectFeatureTaskIssueView(QWidget):
    
    def __init__(self, viewController, model, projectId, search=None, currentIndex=0):
        super().__init__()
        
        self.viewController = viewController
        self.model = model
        self.projectId = projectId
        self.searchText = search 
        self.currentIndex = currentIndex

        self.window = Ui_ProjectFeatureTaskIssueWindow()
        self.window.setupUi(self)
        
            

        with open('QSS\ProjectFeatureTaskIssueStyle.qss', 'r') as file:
            stylesheet = file.read()

        self.setStyleSheet(stylesheet)
        

        # -- Signals ----
        self.window.tabWidget.setCurrentIndex(self.currentIndex)
        self.window.tabWidget.currentChanged.connect(self.tabChanged)
        self.window.BackBtn.clicked.connect(self.goBack) 
        self.window.AddNewBtn.clicked.connect(self.addNew)
        

        self.featureView = None
        self.taskView = None
        self.issueView = None
        
        self.editing = False


        self.getProjectName()
        
        self.createFeatureTabView()
        self.createTaskTabView()
        self.createIssueTabView()
        
                
        self.tabChanged(self.currentIndex)
        


    # ----------------------------------------------------------------------------------------
     
    # -------- FEATURES TAB ----------------------------
    def createFeatureTabView(self, editDict=None):
        
        self.featureView = FeatureTabView(self, 0, editDict)
        self.featureModelResults = self.model.getFeatures(self.projectId, self.searchText)
        self.populateFeatureData()
        self.window.FeaturesTab.layout().addWidget(self.featureView) 


    # -------- TASKS TAB ----------------------------
    def createTaskTabView(self, editDict=None):
        
        self.taskView = TaskTabView(self, 1, editDict)
        self.taskModelResults = self.model.getTasks(self.projectId, self.searchText)
        self.populateTaskData()
        self.window.TasksTab.layout().addWidget(self.taskView) 


    # -------- ISSUES TAB ----------------------------
    def createIssueTabView(self, editDict=None):
        
        self.issueView = IssueTabView(self, 2, editDict)
        self.issueModelResults = self.model.getIssues(self.projectId, self.searchText)
        self.populateIssueData()
        self.window.IssuesTab.layout().addWidget(self.issueView) 
        

    # ----------------------------------------------------------------------------------------
    
    
    def getProjectName(self):
        
        projectName = self.model.getProjectName(self.projectId)
        self.window.TitleLabel.setText(projectName)
     

    # ----------------------------------------------------------------------------------------
    

    def clearLayout(self, layout):
        ic("clearGrids")
        
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()     
    
                
    # ----------------------------------------------------------------------------------------
    
    def populateFeatureData(self):
        ic("populateFeatureData")

        # -- Populate Data --
        for rowIndex, feature in enumerate(self.featureModelResults):
            
            feature["rowId"] = rowIndex + 1
                
            self.featureView.addFeatureToDisplay(feature)            
        

    # ----------------------------------------------------------------------------------------
       
      
    def populateTaskData(self):
        ic("populateTaskData")

        # -- Populate Data --
        for rowIndex, task in enumerate(self.taskModelResults):
            
            # Add a rowId column
            task["rowId"] = rowIndex + 1

            self.taskView.addTaskToDisplay(task)            
     

    # ----------------------------------------------------------------------------------------
        

    def populateIssueData(self):
        ic("populateIssueData")

        # -- Populate Data --
        for rowIndex, issue in enumerate(self.issueModelResults):
            
            issue["rowId"] = rowIndex + 1
                
            self.issueView.addIssueToDisplay(issue)            
        

    # ----------------------------------------------------------------------------------------
    

    def search(self):
        ic("search")
        
        self.searchText = self.window.Input.text()
            
        self.getModel()
        self.loadGrid()
    
        
    # ---------------------------------------------------------------------------------------- 

    def goBack(self):
        ic("goBack")
        
        self.viewController.displayProjectView()
        

    # ---------------------------------------------------------------------------------------- 
    
    
    def getPriorityDict(self):
        
        priorityDict = {1: {"Priority" : "Highest", "Color" : "red"},
                        2: {"Priority" : "High",    "Color" : "orange"},
                        3: {"Priority" : "Medium",  "Color" : "yellow"},
                        4: {"Priority" : "Low",     "Color" : "green"},
                        5: {"Priority" : "Lowest",  "Color" : "white"}}
        

        return priorityDict


    # ---------------------------------------------------------------------------------------- 
    

    def tabChanged(self, index):
        
        self.currentIndex = index
        
        if index == 0:
            self.statusBarMessage = "Features: " + str(len(self.featureModelResults))
            self.viewController.statusBar().showMessage(self.statusBarMessage)
            
        elif index == 1:
            self.statusBarMessage = "Tasks: " + str(len(self.taskModelResults))
            self.viewController.statusBar().showMessage(self.statusBarMessage)
            
        elif index == 2:
            self.statusBarMessage = "Issues: " + str(len(self.issueModelResults))
            self.viewController.statusBar().showMessage(self.statusBarMessage)
            
        self.window.DescriptionTextLabel.setText("")
        
        self.currentIndex = index


    # ---------------------------------------------------------------------------------------- 


    def addNew(self):
        ic("addNew")
        
        if self.currentIndex == 0:
            self.viewController.displayAddNewFeatureView(self, self.projectId)
            
        elif self.currentIndex == 1:
            self.viewController.displayAddNewTaskView(self, self.projectId)
            
        elif self.currentIndex == 2:
            self.viewController.displayAddNewIssueView(self, self.projectId)
        
         
    # ----------------------------------------------------------------------------------------
    


    
