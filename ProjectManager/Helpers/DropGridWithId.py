from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy
from PySide6.QtCore import QDataStream, Qt
from Helpers.DragDropLabel import DragDropLabel
from icecream import ic



class DropGridWithId(QWidget):
    def __init__(self, viewController, model, id=0, objectName=None):
        super().__init__()
        
        self.viewController = viewController
        self.model = model
        self.id = id
        if objectName:
            self.setObjectName(objectName)
        
        self.setAcceptDrops(True)
        
        # Create a grid layout
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.grid.setAlignment(Qt.AlignTop)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


           
    # ----------------------------------------------------------------------------------------
    
    def getId(self):
        return self.id
    
    # ----------------------------------------------------------------------------------------
    
    def dragEnterEvent(self, event):
        ic("gridDrag") 
        event.acceptProposedAction()

    # ----------------------------------------------------------------------------------------
    
    def dropEvent(self, event):
        ic("gridDrop")       

        if isinstance(event.source(), DragDropLabel):
            
            byteArray = event.mimeData().data('application/x-taskData')
            dataStream = QDataStream(byteArray)
            
            projectId = dataStream.readInt32()
            taskId = dataStream.readInt32()
            taskStatus = dataStream.readQString()
            
            # The task is being moved into a different column, therefore taking on a new status
            if event.source() != self:                

                if isinstance(self, DropGridWithId):
                    targetGridId = self.getId()
                    ic(targetGridId)
                
                    taskStatus = ""
                    if targetGridId == 0:
                        taskStatus = "Waiting"
                    elif targetGridId == 1:
                        taskStatus = "InProgress"
                    elif targetGridId == 2:
                        taskStatus = "Complete"

                    self.model.setTaskStatus(projectId, taskId, taskStatus)
                    self.viewController.displayProjectFeatureTaskIssueView(projectId, currentIndex=1)
                    event.acceptProposedAction()
                    
            else:
                # The task is being reordered in the same column. TaskId's will need reordering
                self.viewController.displayProjectFeatureTaskIssueView(projectId, currentIndex=1)