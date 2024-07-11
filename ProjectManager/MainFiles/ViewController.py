from icecream import ic
from PySide6.QtWidgets import QMainWindow, QStatusBar
from PySide6.QtCore import Qt

from UiViews.UiMainWindow import Ui_MainWindow
from Models.ProjectModel import ProjectModel

from Views.ProjectView import ProjectView
from Views.AddNewProjectView import AddNewProjectView
from Views.ProjectFeatureTaskIssueView import ProjectFeatureTaskIssueView
from Views.AddNewFeatureView import AddNewFeatureView
from Views.AddNewTaskView import AddNewTaskView
from Views.AddNewIssueView import AddNewIssueView



class ViewController(QMainWindow):

    
    def __init__(self, main, logController):
        super().__init__()

        self.logController = logController
        self.Main = main
        
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.setWindowTitle("Project Manager")
     

        with open('QSS\style.qss', 'r') as file:
             stylesheet = file.read()

        self.setStyleSheet(stylesheet)
                
        self.hoverEnterStyle = "background-color: #024087;"
        self.backgroundNormalStyle = "background-color: #4b4a4c;"

        # statusbar
        self.setStatusBar(QStatusBar(self))  


        self.projectModel = None

        # ------
        
        self.displayProjectView()


    # ----------------------------------------------------------------------------------------
        

    def main(self):        
        self.show()


    # ----------------------------------------------------------------------------------------

    def displayProjectView(self):
        ic("displayProjectView")
        
        self.projectModel = ProjectModel()
        self.projectView = ProjectView(self, self.projectModel)
        self.window.stackedWidget.addWidget(self.projectView)
        self.window.stackedWidget.setCurrentWidget(self.projectView)
        

    # ----------------------------------------------------------------------------------------
    
    
    def displayProjectFeatureTaskIssueView(self, projectId, search=None, currentIndex=0):
        ic("displayProjectFeatureTaskIssueView")
        
        self.projectModel = ProjectModel()
        self.projectFeatureTaskIssueView = ProjectFeatureTaskIssueView(self, self.projectModel, projectId, search, currentIndex)
        self.window.stackedWidget.addWidget(self.projectFeatureTaskIssueView)
        self.window.stackedWidget.setCurrentWidget(self.projectFeatureTaskIssueView)
     
        
    # ----------------------------------------------------------------------------------------
    
    def displayAddNewProjectView(self):
        self.addNewProjectView = AddNewProjectView(self)
        self.addNewProjectView.main()
    
        
    # ----------------------------------------------------------------------------------------
    

    def addNewProject(self, projectInfoDict):
        self.projectModel.addNewProject(projectInfoDict)
        self.displayProjectView()
        self.addNewProjectView.close()


    # ----------------------------------------------------------------------------------------
    
    
    def displayAddNewFeatureView(self, parentView, projectId):
        self.addNewFeatureView = AddNewFeatureView(self, parentView, projectId)
        self.addNewFeatureView.main()


    def addNewFeature(self, featureInfoDict):
        self.projectModel.addNewFeature(featureInfoDict)
        self.displayProjectFeatureTaskIssueView(featureInfoDict["projectId"], currentIndex=0)
        self.addNewFeatureView.close()


    # ----------------------------------------------------------------------------------------
    
    
    def displayAddNewTaskView(self, parentView, projectId):
        self.addNewTaskView = AddNewTaskView(self, parentView, projectId)
        self.addNewTaskView.main()


    def addNewTask(self, taskInfoDict):
        self.projectModel.addNewTask(taskInfoDict)
        self.displayProjectFeatureTaskIssueView(taskInfoDict["projectId"], currentIndex=1)
        self.addNewTaskView.close()


    # ----------------------------------------------------------------------------------------
    
    
    def displayAddNewIssueView(self, parentView, projectId):
        self.addNewIssueView = AddNewIssueView(self, parentView, projectId)
        self.addNewIssueView.main()


    def addNewIssue(self, issueInfoDict):
        self.projectModel.addNewIssue(issueInfoDict)
        self.displayProjectFeatureTaskIssueView(issueInfoDict["projectId"], currentIndex=2)
        self.addNewIssueView.close()


    # ----------------------------------------------------------------------------------------
    

    def closeDatabase(self):
            
        if self.projectModel:
            self.projectModel.connection.close()
    

    # ----------------------------------------------------------------------------------------
    
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.Main.exit()
        
