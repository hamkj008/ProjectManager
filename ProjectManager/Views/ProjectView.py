from icecream import ic

from UiViews.UiProjectWindow import Ui_ProjectWindow
from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QMessageBox, QPushButton
from PySide6.QtCore import Qt
from functools import partial



# First view presented to user
class ProjectView(QWidget):

    
    def __init__(self, viewController, model):
        super().__init__()
        
        self.viewController = viewController
        self.model = model

        self.window = Ui_ProjectWindow()
        self.window.setupUi(self)
        
        with open('QSS\ProjectViewStyle.qss', 'r') as file:
             stylesheet = file.read()

        self.setStyleSheet(stylesheet)


        # -- Init --
        self.searchText = None
        
        self.window.ProjectGridFrame.layout().setAlignment(Qt.AlignTop)
        self.window.SearchInput.textChanged.connect(self.search)
        self.window.AddNewProjectBtn.clicked.connect(self.addNewProject)

        self.viewController.statusBar().showMessage("")
        
        
        # -- Load Grid --
        self.getModel()
        self.loadGrid() 
        

    # ----------------------------------------------------------------------------------------
     
     
    def getModel(self):
        ic("getModel")

        self.modelResults = self.model.getProjects(self.searchText)


    # ----------------------------------------------------------------------------------------
        

    def loadGrid(self):
        ic("loadGrid")
        
        self.clearGrid()
        self.setUpGrid()
        self.populateData()
        

    # ----------------------------------------------------------------------------------------
        

    def clearGrid(self):
        ic("clearGrid")
        
        grid = self.window.ProjectGridFrame.layout()
        
        while grid.count():
            item = grid.takeAt(0)
            if item.widget():
                item.widget().deleteLater()      
                

    # ----------------------------------------------------------------------------------------


    def setUpGrid(self):
        ic("setUpGrid")

        self.projectHeaderColumnId = {}
        self.projectViewHeaders = {"projectName"    : "Project Name", 
                                    "dateCreated"   : "Date Created",
                                    "delete"        : ""}

        for index, (key, value) in enumerate(self.projectViewHeaders.items()):
            columnTitle = QLabel(value)
            columnTitle.setObjectName("header")
            if key == "projectName":
                columnTitle.setSizePolicy(QSizePolicy.Expanding, columnTitle.sizePolicy().verticalPolicy())
             
                            
            self.window.ProjectGridFrame.layout().addWidget(columnTitle, 0, index)
            
            self.projectHeaderColumnId[key] = index
     

    # ----------------------------------------------------------------------------------------


    def populateData(self):
        ic("populateData")

        # -- Populate Data --
        for rowIndex, project in enumerate(self.modelResults):
            
            project["rowId"] = rowIndex + 1
                
            self.addProjectToDisplay(project)            


        self.statusBarMessage = "Projects: " + str(len(self.modelResults))
        self.viewController.statusBar().showMessage(self.statusBarMessage)
        

    # ----------------------------------------------------------------------------------------


    def addProjectToDisplay(self, project):
        ic("addProject")
        
        labelRowList = []
        
        for key, value in project.items():
            for header in self.projectViewHeaders:
                
                if key in self.projectViewHeaders:
                    label = QLabel(f'{value}')
                    label.setObjectName("projectRow")
                
                    if header == "projectName":
                        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                    
                    label.mousePressEvent = (partial(self.rowClicked, project["projectId"]))
                    self.window.ProjectGridFrame.layout().addWidget(label, project["rowId"], self.projectHeaderColumnId[key])
                    labelRowList.append(label)
                    
                else:
                    # -- Remove Project --
                    if header == "delete":
                        removeBtn = QPushButton("x")    
                        removeBtn.setObjectName("removeBtn")
                        removeBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                        removeBtn.clicked.connect(partial(self.removeProject, project["projectId"]))
                        self.window.ProjectGridFrame.layout().addWidget(removeBtn, project["rowId"], self.projectHeaderColumnId[header])                   
          

        for label in labelRowList:
            label.enterEvent = (partial(self.hoverEnter, labelRowList, project["projectDescription"]))
            label.leaveEvent = (partial(self.hoverLeave, labelRowList))


    # ----------------------------------------------------------------------------------------


    def rowClicked(self, projectId, event):
        ic("rowClicked")
        
        if event.button() == Qt.LeftButton:
            self.viewController.displayProjectFeatureTaskIssueView(projectId)


    # ----------------------------------------------------------------------------------------
    
    
    def hoverEnter(self, labelRowList, projectDescription, event):

        self.window.DescriptionTextLabel.setText(projectDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.backgroundNormalStyle)


    # ----------------------------------------------------------------------------------------
    
    
    def search(self):
        ic("search")
        
        self.searchText = self.window.SearchInput.text()
            
        self.getModel()
        self.loadGrid()
    
        
    # ---------------------------------------------------------------------------------------- 
    
    
    def addNewProject(self):
        ic("addNewProject")
        
        self.viewController.displayAddNewProjectView()
        

    # ---------------------------------------------------------------------------------------- 
    
    
    def removeProject(self, projectId):
        ic("remove project")
        
        messageBox = QMessageBox()
        messageBox.setMinimumSize(200, 200)
        messageBox.setWindowTitle("Delete Project?")
        messageBox.setText("Are you sure you want to delete this project?")
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messageBox.setDefaultButton(QMessageBox.Cancel)
        ret = messageBox.exec()   
        
        if ret == QMessageBox.Ok:
            # Remove task from the database
            self.model.deleteProject(projectId)  
            
            self.viewController.displayProjectView()