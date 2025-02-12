from icecream import ic
from functools import partial

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent
from UiViews.UiProjectWindow import Ui_ProjectWindow
from MyHelperLibrary.Helpers.DataLabel import DataLabel
from MyHelperLibrary.Helpers.HelperMethods import clearLayout, createActionDictionary, addActionToMenu


# ========================================================================================
      

# First view presented to user
class ProjectView(QWidget):

    
    def __init__(self, viewController):
        super().__init__()
        
        self.viewController = viewController

        # ---- SETUP UI -----
        self.window = Ui_ProjectWindow()
        self.window.setupUi(self)
        self.setStyle()


        # ------- Init --------
        self.searchText = None
        
        self.window.ProjectGridFrame.layout().setAlignment(Qt.AlignTop)
        self.window.SearchInput.textChanged.connect(self.search)
        self.window.AddNewBtn.clicked.connect(self.addNew)

        self.viewController.statusBar().showMessage("")
        
        # -----
        
        # -- Start --
        self.loadSelf()
        

    # ========================================================================================
            

    def setStyle(self):
        ic("projectssyle")
        self.setStyleSheet(self.viewController.qssController.getStandardStyle())


    # ========================================================================================
    
    
    def loadSelf(self):

        self.getModel()       
        clearLayout(self.window.ProjectGridFrame.layout())
        self.setupGrid()
        self.populateData()  
     

    # ========================================================================================
     

    def getModel(self):
        ic("getModel")

        self.modelResults = self.viewController.model.getProjects(self.searchText)


    # ========================================================================================


    def setupGrid(self):
        ic("setupGrid")

        self.projectHeaderColumnId = {}
        self.projectViewHeaders = {"projectName"    : "Project Name", 
                                    "dateCreated"   : "Date Created"}

        for index, (key, value) in enumerate(self.projectViewHeaders.items()):
            columnTitle = QLabel(value, objectName="header")
             
            self.window.ProjectGridFrame.layout().addWidget(columnTitle, 0, index)
            
            self.projectHeaderColumnId[key] = index
     

    # ========================================================================================


    def populateData(self):
        ic("populateData")

        # -- Populate Data --
        for rowIndex, project in enumerate(self.modelResults):
            
            project["rowId"] = rowIndex + 1
                
            self.addProjectToDisplay(project)            

        self.statusBarMessage = "Projects: " + str(len(self.modelResults))
        self.viewController.statusBar().showMessage(self.statusBarMessage)
        

    # ========================================================================================


    def addProjectToDisplay(self, project):
        ic("addProject")
        
        labelRowList = []
        
        for key, value in project.items():
                
            if key in self.projectViewHeaders:
                label = DataLabel(f'{value}', project, objectName="row")
                
                if key == "projectName":
                    label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

                if key == "dateCreated":
                    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    
                label.mousePressEvent = (partial(self.rowClicked, project["projectId"]))
                label.installEventFilter(self)
                    
                self.window.ProjectGridFrame.layout().addWidget(label, project["rowId"], self.projectHeaderColumnId[key])
                labelRowList.append(label)             
          
        for label in labelRowList:
            label.enterEvent = (partial(self.hoverEnter, labelRowList, project["projectDescription"]))
            label.leaveEvent = (partial(self.hoverLeave, labelRowList))


    # ========================================================================================


    def rowClicked(self, projectId, event):
        ic("rowClicked")
        
        if event.button() == Qt.LeftButton:
            self.viewController.stateController.projectId = projectId
            self.viewController.displayView("ProjectFeatureTaskIssueView")


    # ========================================================================================
    
    
    def hoverEnter(self, labelRowList, projectDescription, event):

        self.window.DescriptionTextLabel.setText(projectDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.qssController.hoverEnter)


    # ========================================================================================
       

    def hoverLeave(self, labelRowList, event): 
        
        self.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.qssController.hoverLeave)


    # ========================================================================================
    
    
    def search(self):
        ic("search")
        
        self.searchText = self.window.SearchInput.text()
            
        self.loadSelf()
    
        
    # ======================================================================================== 
    
    
    def addNew(self):
        ic("addNew")
        
        self.viewController.displayView("AddNewProjectView", newWindow=True)
        

    # ======================================================================================== 
    
    
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
            self.viewController.model.deleteProject(projectId)  
            
            self.viewController.displayView("ProjectView")
            

    # ======================================================================================== 
 

    # Add right click menus
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
        
            rightMenu = QMenu(self)

            # -- Edit Menu --
            editAction    = createActionDictionary("Edit", trigger=partial(self.editProject, obj.data))
            
            # -- Delete Menu --
            deleteAction  = createActionDictionary("Delete", trigger=partial(self.removeProject, obj.data["projectId"]))
            
            #---------------
            
            actionList = [editAction, "separator", deleteAction]
            addActionToMenu(rightMenu, actionList)

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)
    
    
    # ======================================================================================== 
 

    def editProject(self, project):
        ic("right click")
        
        self.viewController.displayView("AddNewProjectView", project, editing=True, newWindow=True)
        

    # ======================================================================================== 
 