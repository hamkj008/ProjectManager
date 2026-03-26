from icecream import ic
from functools import partial

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QMenu
from PySide6.QtCore import Qt, QEvent

from MainFiles.Mixins.Utility_Mixin import Interaction_Mixin
from UiViews.UiProjectWindow import Ui_ProjectWindow
from MyHelperLibrary.Helpers.DataLabel import DataLabel
from MyHelperLibrary.Helpers.HelperMethods import clearLayout, createActionDictionary, addActionToMenu, getCurrentFunction, createCustomChoiceDialog


# ========================================================================================

# First view presented to user
class ProjectView(QWidget, Interaction_Mixin):

    def __init__(self, viewController):
        super().__init__()
        ic(__class__.__name__)
        
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
        
        self.setStyleSheet(self.viewController.qssController.getStandardStyle())

    # ========================================================================================
    
    def loadSelf(self):

        self.getModel()       
        clearLayout(self.window.ProjectGridFrame.layout())
        self.setupGrid()
        self.populateData()  

    # ========================================================================================

    def getModel(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        self.modelResults = self.viewController.model.getProjects(self.searchText)

    # ========================================================================================

    def setupGrid(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        self.projectHeaderColumnId = {}
        self.projectViewHeaders = {"projectName"    : "Project Name", 
                                    "dateCreated"   : "Date Created"}

        for index, (key, value) in enumerate(self.projectViewHeaders.items()):
            columnTitle = QLabel(value, objectName="header")
            
            self.window.ProjectGridFrame.layout().addWidget(columnTitle, 0, index)
            
            self.projectHeaderColumnId[key] = index

    # ========================================================================================

    def populateData(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        # -- Populate Data --
        for rowIndex, project in enumerate(self.modelResults):
            
            project["rowId"] = rowIndex + 1
                
            self.addProjectToDisplay(project)            

        self.statusBarMessage = "Projects: " + str(len(self.modelResults))
        self.viewController.statusBar().showMessage(self.statusBarMessage)
        

    # ========================================================================================

    def addProjectToDisplay(self, project):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
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
            label.enterEvent = (partial(self.hoverEnter, labelRowList, self.window.DescriptionTextLabel, project["projectDescription"]))
            label.leaveEvent = (partial(self.hoverLeave, labelRowList, self.window.DescriptionTextLabel))

    # ========================================================================================

    def rowClicked(self, projectId, event):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        if event.button() == Qt.LeftButton:
            self.viewController.stateController.projectId = projectId
            self.viewController.displayView("ProjectFeatureTaskIssueView")

    # ========================================================================================
    
    def search(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        self.searchText = self.window.SearchInput.text()
            
        self.loadSelf()
    
    # ======================================================================================== 
    
    def addNew(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        self.viewController.displayView("AddNewProjectView", newWindow=True)
        
    # ======================================================================================== 
    
    def removeProject(self, projectId):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        if createCustomChoiceDialog("Delete Project?", 
                                "Are you sure you want to delete this project?", 400, 300, self.viewController.qssController.getDialogStyle()):

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
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        self.viewController.displayView("AddNewProjectView", project, editing=True, newWindow=True)
        

    # ======================================================================================== 