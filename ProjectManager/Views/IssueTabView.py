from icecream import ic

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QAction
from Helpers.ResizeableGrid import ResizeableGrid
from Helpers.IssueDragDropLabel import IssueDragDropLabel
from Helpers.IssueDropGridWithId import IssueDropGridWithId
from functools import partial


class IssueTabView(QWidget):

    def __init__(self, parentView, tabId, editDict=None):
        super().__init__()
        
        self.parentView = parentView
        self.tabId = tabId
        self.editDict = editDict

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        # Create a resizeable grid layout
        issueResizeableGrid = ResizeableGrid() 
        layout.addWidget(issueResizeableGrid)
        
        # Rebind the grid children to the new grid
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueLabelFrame, 0, 0, 1, 1)
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueCompletedLabelFrame, 0, 1, 1, 1)
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueLeftFrame, 1, 0, 1, 1)
        issueResizeableGrid.layout().addWidget(self.parentView.window.IssueRightFrame, 1, 1, 1, 1)

        # Implement resizing event listeners
        issueResizeableGrid.setFrames([self.parentView.window.IssueLabelFrame, self.parentView.window.IssueLeftFrame, 
                                  self.parentView.window.IssueCompletedLabelFrame, self.parentView.window.IssueRightFrame])


        issueGrid = IssueDropGridWithId(self.parentView.viewController, self.parentView.model, objectName="issueGrid")
        self.parentView.window.IssueScrollAreaContents.layout().addWidget(issueGrid)
        
        issueCompleteGrid = IssueDropGridWithId(self.parentView.viewController, self.parentView.model, 1, objectName="IssueCompleteGridFrame")
        self.parentView.window.IssueCompleteScrollAreaContents.layout().addWidget(issueCompleteGrid)
        
        issueResizeableGrid.enableMouseTrackingRecursive()
        
        self.issueGrids = {"issueGrid"          :   issueGrid, 
                          "issueCompleteGrid"   :   issueCompleteGrid}
        

        self.priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView

        # If an entry is being edited, add the finish button to the display
        if self.editDict and self.editDict["isEditing"]:
            finishEditBtn = QPushButton("Finish Editing", objectName="finishEditBtn")
            finishEditBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.parentView.window.FinishEditFrame.layout().addWidget(finishEditBtn)
            finishEditBtn.clicked.connect(self.editFinished)

        
        self.setUpIssueGrids()

    # ----------------------------------------------------------------------------------------


    def setUpIssueGrids(self):
        ic("setUpIssueGrids")

        self.issueHeaderColumnId = {}
        self.issueViewHeaders = {"issueName"        :   "Issue Summary", 
                                "dateIssueCreated"  :   "Date Created",
                                "priority"          :   "Priority"}

        for gridValue in self.issueGrids.values():
                
            for index, (key, value) in enumerate(self.issueViewHeaders.items()):
                columnTitle = QLabel(value, objectName="header")
                
                if key == "issueName":
                    columnTitle.setSizePolicy(QSizePolicy.Expanding, columnTitle.sizePolicy().verticalPolicy())
         
                gridValue.layout().addWidget(columnTitle, 0, index)
            
                self.issueHeaderColumnId[key] = index
    
            
    # ----------------------------------------------------------------------------------------

    
    def addIssueToDisplay(self, issue):
        ic("addIssueToDisplay")
        
        rowList = []
        labelList = []
        
        for key, value in issue.items():
            if key in self.issueViewHeaders:
                
                if key == "priority":
                    priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
                    priority, color = priorityDict[value]["Priority"], priorityDict[value]["Color"]
                    
                    # Display the priority along with a representative color
                    layout = QHBoxLayout()
                    layout.setContentsMargins(0,0,0,0)
                    layout.setSpacing(0)
                    issueObjectLabel = QFrame()
                    issueObjectLabel.setLayout(layout)
                    
                    # Used to control the size of the color frame
                    colorMasterFrame = QFrame()
                    colorMasterFrame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    colorMasterLayout = QHBoxLayout()
                    colorMasterLayout.setContentsMargins(0,0,0,0)
                    colorMasterFrame.setLayout(colorMasterLayout)
                    
                    # A frame, layout and placeholderlabel form the structure to hold the representative color 
                    colorFrame = QFrame()
                    colorFrame.setStyleSheet(f"background-color: {color};") # Color changes based on priority 
                    colorFrame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    
                    colorFrameLayout = QHBoxLayout()
                    colorFrameLayout.setContentsMargins(0,0,0,0)
                    colorFrame.setLayout(colorFrameLayout)
                    placeholder = QLabel("", objectName="placeholder")
                    placeholder.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    colorFrameLayout.addWidget(placeholder)
                    
                    colorMasterLayout.addWidget(colorFrame)

                    # The priority label
                    priorityLabel = IssueDragDropLabel(priority, self, issue, objectName="taskObjectLabel")
                    labelList.append(priorityLabel)
                    layout.addWidget(priorityLabel)
                    layout.addWidget(colorMasterFrame)

                else:
                    issueObjectLabel = IssueDragDropLabel(value, self, issue)
                    labelList.append(issueObjectLabel)
                  
                # taskObjectLabel used as name for QSS
                issueObjectLabel.setObjectName("taskObjectLabel")

                if issue["isComplete"] == "False":
                    self.issueGrids["issueGrid"].layout().addWidget(issueObjectLabel, issue["rowId"], self.issueHeaderColumnId[key])                   
                    
                elif issue["isComplete"] == "True":
                    self.issueGrids["issueCompleteGrid"].layout().addWidget(issueObjectLabel, issue["rowId"], self.issueHeaderColumnId[key])

                # Add it to the row list
                rowList.append(issueObjectLabel)
                
        self.issueComplete(labelList, issue)
        
        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, issue["issueDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList))  

    # ----------------------------------------------------------------------------------------


    def rowClicked(self, issueDescription, event):   
        ic("rowClicked")
        self.parentView.window.DescriptionTextLabel.setText(issueDescription)
        

    # ----------------------------------------------------------------------------------------


    def hoverEnter(self, labelRowList, issueDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(issueDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.backgroundNormalStyle)


    # ----------------------------------------------------------------------------------------
    
    
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
         
                        
    # ----------------------------------------------------------------------------------------
    

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
            self.parentView.model.deleteIssue(self.parentView.projectId, issueId)  

            # Clear and redisplay issues in grid
            self.parentView.viewController.displayProjectFeatureTaskIssueView(self.parentView.projectId, currentIndex=self.parentView.currentIndex)
            

    # ----------------------------------------------------------------------------------------
            
    
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
            
            rightMenu = QMenu(self)

            # Adding actions to the context menu
            
            # -- Edit Menu --
            edit = QAction("Edit", self)
            edit.triggered.connect(partial(self.editIssue, obj.data))
            rightMenu.addAction(edit)
            
            rightMenu.addSeparator()

            #---------------
            
            # -- Delete Menu --
            delete = QAction("Delete", self)
            delete.triggered.connect(partial(self.removeIssue, obj.data["issueId"]))
            rightMenu.addAction(delete)

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)
    

    # ----------------------------------------------------------------------------------------
    

    def editIssue(self, issue):
        ic("edit Issue")

        self.editDict = {"issueId": issue["issueId"], "rowId": issue["rowId"], "tabId": self.tabId, "isEditing": True}

        self.parentView.createIssueTabView(self.editDict)


    # ----------------------------------------------------------------------------------------


    def editFinished(self):
        ic("editFinished")
        
        selection = 0

        for key, value in self.priorityDict.items():
            if self.prioritySelectionMenu.currentText() == value["Priority"]:
                selection = key
                break
            
        self.parentView.model.updateIssue(self.parentView.projectId, self.editDict["issueId"], self.issueNameInput.text(), selection)
        self.editDict["isEditing"] = False

        # Clear the finish edit button from the display
        self.parentView.clearLayout(self.parentView.window.FinishEditFrame.layout())
        
        # Clear and redisplay tasks in grid
        self.parentView.createIssueTabView(self.editDict)
      
        
    # ----------------------------------------------------------------------------------------