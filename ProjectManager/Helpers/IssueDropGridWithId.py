from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy
from PySide6.QtCore import QDataStream, Qt
from Helpers.IssueDragDropLabel import IssueDragDropLabel
from icecream import ic


# ========================================================================================
      

class IssueDropGridWithId(QWidget):
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


    # ========================================================================================
    
    def getId(self):
        return self.id
    
    # ========================================================================================
    
    def dragEnterEvent(self, event):
        ic("gridDrag") 
        event.acceptProposedAction()

    # ========================================================================================
    
    def dropEvent(self, event):
        ic("gridDrop")       

        if isinstance(event.source(), IssueDragDropLabel):
            
            byteArray = event.mimeData().data('application/x-issueData')
            dataStream = QDataStream(byteArray)
            
            projectId = dataStream.readInt32()
            issueId = dataStream.readInt32()
            isComplete = dataStream.readQString()
            
            # The task is being moved into a different column, therefore taking on a new status
            if event.source() != self:                

                if isinstance(self, IssueDropGridWithId):
                    targetGridId = self.getId()
                
                    isComplete = ""
                    if targetGridId == 0:
                        isComplete = "False"
                    elif targetGridId == 1:
                        isComplete = "True"

                    self.model.updateCompleteIssue(issueId, isComplete)
                    self.viewController.displayView("ProjectFeatureTaskIssueView", currentIndex=2)
                    event.acceptProposedAction()
                    
            else:
                # The task is being reordered in the same column. TaskId's will need reordering
                self.viewController.displayView("ProjectFeatureTaskIssueView", currentIndex=2)
