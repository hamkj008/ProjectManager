from icecream import ic
from functools import partial

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent
from MyHelperLibrary.Helpers.ResizableGrid import ResizeableGrid
from Helpers.IssueDragDropLabel import IssueDragDropLabel
from Helpers.IssueDropGridWithId import IssueDropGridWithId
from MyHelperLibrary.Helpers.HelperMethods import createActionDictionary, addActionToMenu, createLayoutFrame, clearLayout


# ========================================================================================
      

class IssueTabView(QWidget):

    def __init__(self, parentView, tabId, editDict=None):
        super().__init__()
        
        self.parentView = parentView
        self.tabId = tabId
        self.editDict = editDict

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        # Create a resizeable grid layout
        dividers = [(self.parentView.window.IssueLabelFrame,    self.parentView.window.IssueCompletedLabelFrame),
                    (self.parentView.window.IssueLeftFrame,     self.parentView.window.IssueRightFrame)] 

        issueResizeableGrid = ResizeableGrid(dividers=dividers) 
        layout.addWidget(issueResizeableGrid)
        
        # Rebind the grid children to the new grid
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueLabelFrame, 0, 0)
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueCompletedLabelFrame, 0, 1)
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueLeftFrame, 1, 0)
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueRightFrame, 1, 1)

        issueGrid           = IssueDropGridWithId(self.parentView.viewController, self.parentView.viewController.model, objectName="issueGrid")
        issueCompleteGrid   = IssueDropGridWithId(self.parentView.viewController, self.parentView.viewController.model, 1, objectName="IssueCompleteGridFrame")
        
        self.issueGrids = {"issueGrid"          :   issueGrid, 
                          "issueCompleteGrid"   :   issueCompleteGrid}
        
        # Add the grids to the parent
        self.parentView.window.IssueScrollAreaContents.layout().addWidget(self.issueGrids["issueGrid"])
        self.parentView.window.IssueCompleteScrollAreaContents.layout().addWidget(self.issueGrids["issueCompleteGrid"])


        self.priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView

        # --- Start ----
        self.loadSelf()
        

    # ========================================================================================


    def loadSelf(self):

        self.getModel()
        
        # Clear the grid panels
        clearLayout(self.issueGrids["issueGrid"].layout())
        clearLayout(self.issueGrids["issueCompleteGrid"].layout())

        self.setUpIssueGrids()
        self.populateIssueData()
        

    # ========================================================================================

            
    def getModel(self):
        self.issueModelResults = self.parentView.viewController.model.getIssues(self.parentView.viewController.stateController.projectId)


    # ========================================================================================


    def setUpIssueGrids(self):
        ic("setUpIssueGrids")

        self.issueHeaderColumnId    = {}
        self.issueViewHeaders       = {"issueName"          :   "Issue Summary", 
                                        "dateIssueCreated"  :   "Date Created",
                                        "priority"          :   "Priority"}

        for gridValue in self.issueGrids.values():
                
            for index, (key, value) in enumerate(self.issueViewHeaders.items()):
                columnTitle = QLabel(value, objectName="header")
                
                if key == "issueName":
                    columnTitle.setSizePolicy(QSizePolicy.Expanding, columnTitle.sizePolicy().verticalPolicy())
         
                gridValue.layout().addWidget(columnTitle, 0, index)
            
                self.issueHeaderColumnId[key] = index
    
            
    # ========================================================================================


    def populateIssueData(self):
        ic("populateIssueData")

        # -- Populate Data --
        for rowIndex, issue in enumerate(self.issueModelResults):
            
            issue["rowId"] = rowIndex + 1
                
            self.addIssueToDisplay(issue)   
            
        statusBarMessage = "Issues: " + str(len(self.issueModelResults))
        self.parentView.viewController.statusBar().showMessage(statusBarMessage)
            
    # ========================================================================================


    def addIssueToDisplay(self, issue):
        ic("addIssueToDisplay")
        
        rowList     = []
        labelList   = []
        
        for key, value in issue.items():
            if key in self.issueViewHeaders:
                           
                if key == "priority":
                    priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
                    priority, color = priorityDict[value]["Priority"], priorityDict[value]["Color"]
                    
                    # Display the priority along with a representative color
                    issueObjectLabel = createLayoutFrame(objectName= "taskLabel", margins=(0,0,0,0))
                    issueObjectLabel.layout().setSpacing(0)
                    
                    # A frame, layout and placeholderlabel form the structure to hold the representative color 
                    colorFrame = createLayoutFrame(sizePolicy=("fixed", "fixed"), margins=(0,0,0,0))
                    colorFrame.setStyleSheet(f"background-color: {color}; border-radius: 10px;") # Color changes based on priority 
                    colorFrame.setFixedSize(20, 20)

                    # The priority label
                    priorityLabel = IssueDragDropLabel(priority, self, issue, objectName="taskLabel")
                    labelList.append(priorityLabel)
                    issueObjectLabel.layout().addWidget(priorityLabel)
                    issueObjectLabel.layout().addWidget(colorFrame)

                # Other keys
                else:
                    issueObjectLabel = IssueDragDropLabel(value, self, issue, objectName="taskLabel")
                    labelList.append(issueObjectLabel)
                  
                issueObjectLabel.installEventFilter(self)
                self.addToGrid(issueObjectLabel, issue, key)                   
                rowList.append(issueObjectLabel)
                
        self.issueComplete(labelList, issue)
        
        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, issue["issueDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList))  


    # ========================================================================================


    def addToGrid(self, label, issue, key):

        isComplete = issue["isComplete"] == "True"      #convert sql boolean placeholder to actual truthy boolean
        
        if isComplete:
            self.issueGrids["issueCompleteGrid"].layout().addWidget(label, issue["rowId"], self.issueHeaderColumnId[key])
        else:
            self.issueGrids["issueGrid"].layout().addWidget(label, issue["rowId"], self.issueHeaderColumnId[key])          


    # ========================================================================================


    def rowClicked(self, issueDescription, event):   

        self.parentView.window.DescriptionTextLabel.setText(issueDescription)
        

    # ========================================================================================


    def hoverEnter(self, labelRowList, issueDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(issueDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.qssController.hoverEnter)


    # ========================================================================================
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.qssController.hoverLeave)


    # ========================================================================================
    
    
    def issueComplete(self, labelList, issue):
        
        # If the task has been marked for completion, a strikethrough will be marked on the text
        if issue["isComplete"] == "True":
            
            # Add the strike through
            for label in labelList:
                label.setText(f"<s>{label.text()}</s>")
                label.installEventFilter(self)
        
        else:
            # remove the strikethrough
            for label in labelList:
                label.setText(f"{label.text()}")
         
                        
    # ========================================================================================
    

    def removeIssue(self, issueId):
        
        messageBox = QMessageBox()
        messageBox.setMinimumSize(200, 200)
        messageBox.setWindowTitle("Delete Issue?")
        messageBox.setText("Are you sure you want to delete this issue?")
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messageBox.setDefaultButton(QMessageBox.Cancel)
        ret = messageBox.exec()
        
        if ret == QMessageBox.Ok:
            # Remove issue from the database
            self.parentView.viewController.model.deleteIssue(issueId)  

            # Clear and redisplay issues in grid
            self.parentView.setActiveWindow(self.tabId)
            

    # ========================================================================================
            
    
    # Adding actions to the right-click context menu
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
            
            rightMenu = QMenu(self)
            
            # -- Edit Menu --
            editAction = createActionDictionary("Edit", trigger=partial(self.editIssue, obj.data))
            
            # -- Delete Menu --
            deleteAction = createActionDictionary("Delete", trigger=partial(self.removeIssue, obj.data["issueId"]))
            
            actionList = [editAction, "separator", deleteAction]
            addActionToMenu(rightMenu, actionList)

            #---------------

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)
    

    # ========================================================================================
    

    def editIssue(self, issue):
        ic("edit Issue")

        self.parentView.viewController.displayView("AddNewView", self.parentView, self.tabId, issue, editing=True, newWindow=True)


    # ========================================================================================