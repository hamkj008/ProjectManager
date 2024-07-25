from icecream import ic

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QFrame, QHBoxLayout, QMessageBox, QPushButton, QMenu
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QAction
from Helpers.ResizeableGrid import ResizeableGrid
from Helpers.DragDropLabel import DragDropLabel
from Helpers.DropGridWithId import DropGridWithId
from functools import partial



class TaskTabView(QWidget):
    
    def __init__(self, parentView, tabId, editDict=None):
        super().__init__()
        
        self.parentView = parentView
        self.tabId = tabId
        self.editDict = editDict

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        # Create a resizeable grid layout
        taskResizeableGrid = ResizeableGrid() 
        layout.addWidget(taskResizeableGrid)
        
        # Rebind the grid children to the new grid
        taskResizeableGrid.layout().addWidget(self.parentView.window.TasksLabelFrame, 0, 0, 1, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskInProgressLabelFrame, 0, 1, 1, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskCompletedLabelFrame, 0, 2, 1, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskLeftFrame, 1, 0, 1, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskCentralFrame, 1, 1, 1, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskRightFrame, 1, 2, 1, 1)

        # Implement resizing event listeners
        taskResizeableGrid.setFrames([self.parentView.window.TasksLabelFrame, self.parentView.window.TaskLeftFrame, self.parentView.window.TaskInProgressLabelFrame, 
                                  self.parentView.window.TaskCentralFrame, self.parentView.window.TaskCompletedLabelFrame, self.parentView.window.TaskRightFrame])

        # DropGridWithId allows the dragdrop labels to be dropped
        taskGrid = DropGridWithId(self.parentView.viewController, self.parentView.model, objectName="TaskGrid")
        self.parentView.window.TaskScrollAreaContents.layout().addWidget(taskGrid)
        
        taskInProgressGrid = DropGridWithId(self.parentView.viewController, self.parentView.model, 1, objectName="TaskInProgressGridFrame")
        self.parentView.window.TaskInProgressScrollAreaContents.layout().addWidget(taskInProgressGrid)
        
        taskCompleteGrid = DropGridWithId(self.parentView.viewController, self.parentView.model, 2, objectName="TaskCompleteGridFrame")
        self.parentView.window.TaskCompleteScrollAreaContents.layout().addWidget(taskCompleteGrid)
        
        taskResizeableGrid.enableMouseTrackingRecursive()
        
        self.taskGrids = {"taskGrid"            :   taskGrid, 
                          "taskInProgressGrid"  :   taskInProgressGrid, 
                          "taskCompleteGrid"    :   taskCompleteGrid}
        
        
        self.priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView

        # If an entry is being edited, add the finish button to the display
        if self.editDict and self.editDict["isEditing"]:
            finishEditBtn = QPushButton("Finish Editing", objectName="finishEditBtn")
            finishEditBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.parentView.window.FinishEditFrame.layout().addWidget(finishEditBtn)
            finishEditBtn.clicked.connect(self.editFinished)
            

        self.setUpTaskGrids()

    # ----------------------------------------------------------------------------------------
    

    def setUpTaskGrids(self):
        ic("setUpTaskGrids")

        self.taskHeaderColumnId = {}
        self.taskViewHeaders = {"taskName"          :   "Task Summary", 
                                "dateTaskCreated"   :   "Date Created",
                                "priority"          :   "Priority"}

        for gridValue in self.taskGrids.values():
                
            for index, (key, value) in enumerate(self.taskViewHeaders.items()):
                columnTitle = QLabel(value, objectName="header")
                
                if key == "taskName":
                    columnTitle.setSizePolicy(QSizePolicy.Expanding, columnTitle.sizePolicy().verticalPolicy())
             
                gridValue.layout().addWidget(columnTitle, 0, index)
            
                self.taskHeaderColumnId[key] = index
    
            
    # ----------------------------------------------------------------------------------------

    
    def addTaskToDisplay(self, task):
        ic("addTaskToDisplay")

        rowList = []
        labelList = []
        
        for key, value in task.items():
            if key in self.taskViewHeaders:
                
                if key == "priority":
                    priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
                    priority, color = priorityDict[value]["Priority"], priorityDict[value]["Color"]
                    
                    # Display the priority along with a representative color
                    layout = QHBoxLayout()
                    layout.setContentsMargins(0,0,0,0)
                    layout.setSpacing(0)
                    taskObjectLabel = QFrame()
                    taskObjectLabel.setLayout(layout)
                    
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
                    placeholder = QLabel("", objectName = "placeholder")
                    placeholder.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    colorFrameLayout.addWidget(placeholder)
                    
                    colorMasterLayout.addWidget(colorFrame)

                    # The priority label
                    priorityLabel = DragDropLabel(priority, self, task, objectName = "taskObjectLabel")
                    labelList.append(priorityLabel)
                    layout.addWidget(priorityLabel)
                    layout.addWidget(colorMasterFrame)

                else:                       
                    taskObjectLabel = DragDropLabel(value, self, task)
                    labelList.append(taskObjectLabel)
                    
                taskObjectLabel.setObjectName("taskObjectLabel")

                if task["taskStatus"] == "Waiting":
                    self.taskGrids["taskGrid"].layout().addWidget(taskObjectLabel, task["rowId"], self.taskHeaderColumnId[key])
                    
                elif task["taskStatus"] == "InProgress":
                    self.taskGrids["taskInProgressGrid"].layout().addWidget(taskObjectLabel, task["rowId"], self.taskHeaderColumnId[key])
                    
                elif task["taskStatus"] == "Complete":
                    self.taskGrids["taskCompleteGrid"].layout().addWidget(taskObjectLabel, task["rowId"], self.taskHeaderColumnId[key])

                # Add it to the row list
                rowList.append(taskObjectLabel)
          
        self.taskComplete(labelList, task)
        
        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, task["taskDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList))  
            

    # ----------------------------------------------------------------------------------------
    
    
    def rowClicked(self, taskDescription, event):   
        ic("rowClicked")
        self.parentView.window.DescriptionTextLabel.setText(taskDescription)
        

    # ----------------------------------------------------------------------------------------


    def hoverEnter(self, labelRowList, taskDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(taskDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.backgroundNormalStyle)


    # ----------------------------------------------------------------------------------------
    
    
    def taskComplete(self, labelList, task):
        
        # If the task has been marked for completion, a strikethrough will be marked on the text
        if task["taskStatus"] == "Complete":
            
            self.parentView.model.updateCompleteTask(self.parentView.projectId, task["taskId"], True)
            task["isComplete"] = 'True'
            
            # Add the strike through
            for label in labelList:
                label.setText(f"<s>{label.text()}</s>")
                label.installEventFilter(self)
        
        else:
            self.parentView.model.updateCompleteTask(self.parentView.projectId, task["taskId"], True)
            task["isComplete"] = 'False'
            
            # remove the strikethrough
            for label in labelList:
                label.setText(f"{label.text()}")
         
                        
    # ----------------------------------------------------------------------------------------


    def removeTask(self, taskId):
        
        messageBox = QMessageBox()
        messageBox.setMinimumSize(200, 200)
        messageBox.setWindowTitle("Delete Task?")
        messageBox.setText("Are you sure you want to delete this task?")
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messageBox.setDefaultButton(QMessageBox.Cancel)
        ret = messageBox.exec()
        
        if ret == QMessageBox.Ok:
            # Remove task from the database
            self.parentView.model.deleteTask(self.parentView.projectId, taskId)  

            # Clear and redisplay tasks in grid
            self.parentView.viewController.displayProjectFeatureTaskIssueView(self.parentView.projectId, currentIndex=self.parentView.currentIndex)
     
            
    # ----------------------------------------------------------------------------------------
    
    
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
            
            rightMenu = QMenu(self)

            # Adding actions to the context menu
            
            # -- Edit Menu --
            edit = QAction("Edit", self)
            edit.triggered.connect(partial(self.editTask, obj.data))
            rightMenu.addAction(edit)
            
            rightMenu.addSeparator()

            #---------------
            
            # -- Delete Menu --
            delete = QAction("Delete", self)
            delete.triggered.connect(partial(self.removeTask, obj.data["taskId"]))
            rightMenu.addAction(delete)

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)


    # ----------------------------------------------------------------------------------------
    

    def editTask(self, task):
        ic("right click")

        self.editDict = {"taskId": task["taskId"], "rowId": task["rowId"], "tabId": self.tabId, "isEditing": True}

        self.parentView.createTaskTabView(self.editDict)


    # ----------------------------------------------------------------------------------------


    def editFinished(self):
        ic("editFinished")
        
        selection = 0

        for key, value in self.priorityDict.items():
            if self.prioritySelectionMenu.currentText() == value["Priority"]:
                selection = key
                break
            
        self.parentView.model.updateTask(self.parentView.projectId, self.editDict["taskId"], self.taskNameInput.text(), selection)
        self.editDict["isEditing"] = False

        # Clear the finish edit button from the display
        self.parentView.clearLayout(self.parentView.window.FinishEditFrame.layout())
        
        # Clear and redisplay tasks in grid
        self.parentView.createTaskTabView(self.editDict)
      
        
    # ----------------------------------------------------------------------------------------