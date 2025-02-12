from icecream import ic
from functools import partial

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QHBoxLayout, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent

from MyHelperLibrary.Helpers.HelperMethods import createActionDictionary, addActionToMenu, createLayoutFrame, clearLayout
from MyHelperLibrary.Helpers.ResizableGrid import ResizeableGrid
from Helpers.DragDropLabel import DragDropLabel
from Helpers.DropGridWithId import DropGridWithId

# ========================================================================================
      

class TaskTabView(QWidget):
    
    def __init__(self, parentView, tabId):
        super().__init__()
        
        self.parentView = parentView
        self.tabId = tabId

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)


        dividers = [(self.parentView.window.TasksLabelFrame,            self.parentView.window.TaskInProgressLabelFrame), 
                    (self.parentView.window.TaskLeftFrame,              self.parentView.window.TaskCentralFrame),
                    (self.parentView.window.TaskInProgressLabelFrame,   self.parentView.window.TaskCompletedLabelFrame),
                    (self.parentView.window.TaskCentralFrame,           self.parentView.window.TaskRightFrame)]

        # Create a resizeable grid layout
        taskResizeableGrid = ResizeableGrid(dividers=dividers) 
        layout.addWidget(taskResizeableGrid)
        
        # Rebind the grid children to the new grid
        taskResizeableGrid.layout().addWidget(self.parentView.window.TasksLabelFrame, 0, 0)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskInProgressLabelFrame, 0, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskCompletedLabelFrame, 0, 2)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskLeftFrame, 1, 0)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskCentralFrame, 1, 1)
        taskResizeableGrid.layout().addWidget(self.parentView.window.TaskRightFrame, 1, 2)


        # DropGridWithId allows the dragdrop labels to be dropped
        taskGrid            = DropGridWithId(self.parentView.viewController, self.parentView.viewController.model, objectName="TaskGrid")
        taskInProgressGrid  = DropGridWithId(self.parentView.viewController, self.parentView.viewController.model, 1, objectName="TaskInProgressGridFrame")
        taskCompleteGrid    = DropGridWithId(self.parentView.viewController, self.parentView.viewController.model, 2, objectName="TaskCompleteGridFrame")
        
        
        self.taskGrids = {"taskGrid"            :   taskGrid, 
                          "taskInProgressGrid"  :   taskInProgressGrid, 
                          "taskCompleteGrid"    :   taskCompleteGrid}
        
        # Add the grids to the parent
        self.parentView.window.TaskScrollAreaContents.layout().addWidget(self.taskGrids["taskGrid"])
        self.parentView.window.TaskInProgressScrollAreaContents.layout().addWidget(self.taskGrids["taskInProgressGrid"])
        self.parentView.window.TaskCompleteScrollAreaContents.layout().addWidget(self.taskGrids["taskCompleteGrid"])

        
        self.priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
        self.searchText = None
        
        # -- Start --
        self.loadSelf()
        
    # ========================================================================================
    

    def loadSelf(self):

        self.getModel()
        
        # Clear the grid panels
        clearLayout(self.taskGrids["taskGrid"].layout())
        clearLayout(self.taskGrids["taskInProgressGrid"].layout())
        clearLayout(self.taskGrids["taskCompleteGrid"].layout())
        
        self.setupGrids()
        self.populateTaskData()
    
    # ========================================================================================
    

    def getModel(self):

        self.taskModelResults = self.parentView.viewController.model.getTasks(self.parentView.viewController.stateController.projectId, self.searchText)


    # ========================================================================================
    

    def setupGrids(self):

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
    
            
    # ========================================================================================

    
    def populateTaskData(self):
        ic("populateTaskData")

        # -- Populate Data --
        for rowIndex, task in enumerate(self.taskModelResults):
            
            # Add a rowId column
            task["rowId"] = rowIndex + 1

            self.addTaskToDisplay(task)            
     
        statusBarMessage = "Tasks: " + str(len(self.taskModelResults))
        self.parentView.viewController.statusBar().showMessage(statusBarMessage)
        

    # ========================================================================================
    
    
    def addTaskToDisplay(self, task):
        ic("addTaskToDisplay")

        rowList     = []    # The list of labels that will respond to hover events
        labelList   = []    # The list of labels that will have the strikethrough applied on completion
        
        for key, value in task.items():
            if key in self.taskViewHeaders:
                
                if key == "priority":
                    priorityDict    = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
                    priority, color = priorityDict[value]["Priority"], priorityDict[value]["Color"]
                    
                    # Display the priority along with a representative color
                    taskLabel = createLayoutFrame(objectName="taskLabel", margins=(0,0,0,0))
                    taskLabel.layout().setSpacing(0)

                    # A frame, layout and placeholderlabel form the structure to hold the representative color 
                    colorFrame = createLayoutFrame(sizePolicy=("fixed", "fixed"), margins=(0,0,0,0))
                    colorFrame.setStyleSheet(f"background-color: {color}; border-radius: 10px;") # Color changes based on priority 
                    colorFrame.setFixedSize(20, 20)                    

                    # The priority label
                    priorityLabel = DragDropLabel(priority, self, task, objectName="taskLabel")
                    taskLabel.layout().addWidget(priorityLabel)
                    taskLabel.layout().addWidget(colorFrame)

                    labelList.append(priorityLabel)

                # Other keys
                else:
                    taskLabel = DragDropLabel(value, self, task, objectName="taskLabel")
                    labelList.append(taskLabel)                   
                
                taskLabel.installEventFilter(self)
                self.addToGrid(taskLabel, task, key)
                rowList.append(taskLabel)
          
        self.taskComplete(labelList, task)
        
        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, task["taskDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList))  
            

    # ========================================================================================
    
    def addToGrid(self, label, task, key):
        
        if task["taskStatus"]   == "Waiting":
            self.taskGrids["taskGrid"].layout().addWidget(label, task["rowId"], self.taskHeaderColumnId[key])
                    
        elif task["taskStatus"] == "InProgress":
            self.taskGrids["taskInProgressGrid"].layout().addWidget(label, task["rowId"], self.taskHeaderColumnId[key])
                    
        elif task["taskStatus"] == "Complete":
            self.taskGrids["taskCompleteGrid"].layout().addWidget(label, task["rowId"], self.taskHeaderColumnId[key])
    

    # ========================================================================================
    

    def rowClicked(self, taskDescription, event):   
        ic("rowClicked")
        
        self.parentView.window.DescriptionTextLabel.setText(taskDescription)
        

    # ========================================================================================


    def hoverEnter(self, labelRowList, taskDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(taskDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.qssController.hoverEnter)


    # ========================================================================================
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.qssController.hoverLeave)


    # ========================================================================================
    
    
    def taskComplete(self, labelList, task):
        
        # If the task has been marked for completion, a strikethrough will be marked on the text
        if task["taskStatus"] == "Complete":
            
            self.parentView.viewController.model.updateCompleteTask(task["taskId"], True)
            task["isComplete"] = 'True'
            
            # Add the strike through
            for label in labelList:
                label.setText(f"<s>{label.text()}</s>")
                label.installEventFilter(self)
        
        else:
            self.parentView.viewController.model.updateCompleteTask(task["taskId"], True)
            task["isComplete"] = 'False'
            
            # remove the strikethrough
            for label in labelList:
                label.setText(f"{label.text()}")
         
                        
    # ========================================================================================


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
            self.parentView.viewController.model.deleteTask(taskId)  

            # Clear and redisplay tasks in grid
            self.parentView.setActiveWindow(self.tabId)
     
            
    # ========================================================================================
    
    # Adding actions to the right-click context menu
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
            
            rightMenu       = QMenu(self)
            
            # -- Edit Menu --
            editAction      = createActionDictionary("Edit", trigger=partial(self.editTask, obj.data))
            
            # -- Delete Menu --
            deleteAction    = createActionDictionary("Delete", trigger=partial(self.removeTask, obj.data["taskId"]))
            
            actionList      = [editAction, "separator", deleteAction]
            addActionToMenu(rightMenu, actionList)

            #---------------

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)


    # ========================================================================================
    

    def editTask(self, task):
        ic("right click")

        self.parentView.viewController.displayView("AddNewView", self.parentView, self.tabId, task, editing=True, newWindow=True)


    # ========================================================================================