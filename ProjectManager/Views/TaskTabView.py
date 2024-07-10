from icecream import ic

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QFrame, QHBoxLayout, QMessageBox, QPushButton
from PySide6.QtCore import Qt
from Helpers.ResizeableGrid import ResizeableGrid
from Helpers.DragDropLabel import DragDropLabel
from Helpers.DropGridWithId import DropGridWithId
from functools import partial


class TaskTabView(QWidget):

    
    def __init__(self, parentView, window, viewController, projectId, model):
        super().__init__()
        
        self.parentView = parentView
        self.window = window
        self.viewController = viewController
        self.projectId = projectId
        self.model = model

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        # Create a resizeable grid layout
        taskResizeableGrid = ResizeableGrid() 
        layout.addWidget(taskResizeableGrid)
        
        # Rebind the grid children to the new grid
        taskResizeableGrid.layout().addWidget(self.window.TasksLabelFrame, 0, 0, 1, 1)
        taskResizeableGrid.layout().addWidget(self.window.TaskInProgressLabelFrame, 0, 1, 1, 1)
        taskResizeableGrid.layout().addWidget(self.window.TaskCompletedLabelFrame, 0, 2, 1, 1)
        taskResizeableGrid.layout().addWidget(self.window.TaskLeftFrame, 1, 0, 1, 1)
        taskResizeableGrid.layout().addWidget(self.window.TaskCentralFrame, 1, 1, 1, 1)
        taskResizeableGrid.layout().addWidget(self.window.TaskRightFrame, 1, 2, 1, 1)

        # Implement resizing event listeners
        taskResizeableGrid.setFrames([self.window.TasksLabelFrame, self.window.TaskLeftFrame, self.window.TaskInProgressLabelFrame, 
                                  self.window.TaskCentralFrame, self.window.TaskCompletedLabelFrame, self.window.TaskRightFrame])

        # 
        taskGrid = DropGridWithId(self.viewController, self.model)
        taskGrid.setObjectName("TaskGrid")
        ic(taskGrid.objectName())
        self.window.TaskScrollAreaContents.layout().addWidget(taskGrid)
        
        taskInProgressGrid = DropGridWithId(self.viewController, self.model, 1)
        taskInProgressGrid.setObjectName("TaskInProgressGridFrame")
        self.window.TaskInProgressScrollAreaContents.layout().addWidget(taskInProgressGrid)
        
        taskCompleteGrid = DropGridWithId(self.viewController, self.model, 2)
        taskCompleteGrid.setObjectName("TaskCompleteGridFrame")
        self.window.TaskCompleteScrollAreaContents.layout().addWidget(taskCompleteGrid)
        
        taskResizeableGrid.enableMouseTrackingRecursive()
        
        self.taskGrids = {"taskGrid"            :   taskGrid, 
                          "taskInProgressGrid"  :   taskInProgressGrid, 
                          "taskCompleteGrid"    :   taskCompleteGrid}
        

    # ----------------------------------------------------------------------------------------
        

    def loadGrids(self):
        ic("loadGrids")

        self.clearGrids()
        self.setUpTaskGrids()

        # self.populateTaskData()
        

    # ----------------------------------------------------------------------------------------
        

    def clearGrids(self):
        ic("clearGrids")
        
        for grid in self.taskGrids.values():
            layout = grid.layout()
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()      
                

    # ----------------------------------------------------------------------------------------
    

    def setUpTaskGrids(self):
        ic("setUpTaskGrids")

        self.taskHeaderColumnId = {}
        self.taskViewHeaders = {"taskName"          :   "Task Summary", 
                                "dateTaskCreated"   :   "Date Created",
                                "priority"          :   "Priority"}

        for gridKey, gridValue in self.taskGrids.items():
            if gridKey == "taskCompleteGrid":
                self.taskViewHeaders["delete"] = ""
                
            for index, (key, value) in enumerate(self.taskViewHeaders.items()):
                columnTitle = QLabel(value)
                columnTitle.setObjectName("header")
                
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
                    placeholder = QLabel("")
                    placeholder.setObjectName("placeholder")
                    placeholder.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    colorFrameLayout.addWidget(placeholder)
                    
                    colorMasterLayout.addWidget(colorFrame)

                    # The priority label
                    priorityLabel = DragDropLabel(priority, self, task)
                    priorityLabel.setObjectName("taskObjectLabel")
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
        self.window.DescriptionTextLabel.setText(taskDescription)
        

    # ----------------------------------------------------------------------------------------


    def hoverEnter(self, labelRowList, taskDescription, event):
        
        self.window.DescriptionTextLabel.setText(taskDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.backgroundNormalStyle)


    # ----------------------------------------------------------------------------------------
    
    
    def taskComplete(self, labelList, task):
        
        # If the task has been marked for completion, a strikethrough will be marked on the text
        if task["taskStatus"] == "Complete":
            
            self.model.updateCompleteTask(self.projectId, task["taskId"], True)
            task["isComplete"] = 'True'
            
            # -- Remove Task --
            removeBtn = QPushButton("x")    
            removeBtn.setObjectName("removeBtn")
            removeBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            removeBtn.clicked.connect(partial(self.removeTask, task["taskId"]))
            self.taskGrids["taskCompleteGrid"].layout().addWidget(removeBtn, task["rowId"], self.taskHeaderColumnId["delete"])
            
            # Add the strike through
            for label in labelList:
                label.setText(f"<s>{label.text()}</s>")
        
        else:
            self.model.updateCompleteTask(self.projectId, task["taskId"], True)
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
            self.model.deleteTask(self.projectId, taskId)  

            # Clear and redisplay tasks in grid
            self.viewController.displayProjectFeatureTaskIssueView(self.projectId, currentIndex=self.parentView.currentIndex)