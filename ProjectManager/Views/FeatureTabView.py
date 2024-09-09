from icecream import ic
from functools import partial

from PySide6.QtWidgets import QLineEdit, QWidget, QLabel, QHBoxLayout, QGridLayout, QMessageBox, QMenu, QComboBox
from PySide6.QtCore import Qt, QEvent
from MyHelperLibrary.Helpers.DataLabel import DataLabel
from MyHelperLibrary.Helpers.HelperMethods import createActionDictionary, addActionToMenu, createLayoutFrame, createWidget, clearLayout


# ========================================================================================
   

class FeatureTabView(QWidget):

    def __init__(self, parentView, tabId, editDict=None):
        super().__init__()
        
        self.parentView = parentView
        self.tabId = tabId
        self.editDict = editDict
        
        # -----------
        
        # Create a new grid layout because will the parent will be cleared each time
        self.featureGrid = QGridLayout()
        self.setLayout(self.featureGrid)
        self.featureGrid.setAlignment(Qt.AlignTop)
        
        # -----------

        self.priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView      
        
        # -- Start --
        self.loadSelf()

    # ========================================================================================


    def loadSelf(self):
        
        self.getModel()
        clearLayout(self.featureGrid)
        self.setupGrid()
        self.populateData()

    # ========================================================================================


    def getModel(self):
        self.modelResults = self.parentView.viewController.model.getFeatures(self.parentView.viewController.stateController.projectId)


    # ========================================================================================


    def setupGrid(self):
        ic("setupGrid")

        self.featureHeaderColumnId = {}
        self.featureViewHeaders = {"featureName"            : "Feature Summary", 
                                    "dateFeatureCreated"    : "Date Created",
                                    "priority"              : "Priority"}

        for index, (key, value) in enumerate(self.featureViewHeaders.items()):
            columnTitle = QLabel(value, objectName="header")
            
            self.featureGrid.addWidget(columnTitle, 0, index)
            self.featureHeaderColumnId[key] = index
   
            
    # ========================================================================================


    def populateData(self):
        ic("populateData")

        # -- Populate Data --
        for rowIndex, feature in enumerate(self.modelResults):
            
            feature["rowId"] = rowIndex + 1
                
            self.addFeatureToDisplay(feature)  
            
        statusBarMessage = "Features: " + str(len(self.modelResults))
        self.parentView.viewController.statusBar().showMessage(statusBarMessage)


    # ========================================================================================
         
    
    def addFeatureToDisplay(self, feature):
        ic("addFeatureToDisplay")
                
        rowList = []
        
        for key, value in feature.items():           
            if key in self.featureViewHeaders:

                if key == "priority":
                    priority, color = self.priorityDict[value]["Priority"], self.priorityDict[value]["Color"]
                        
                    # Display the priority along with a representative color
                    taskLabel = createLayoutFrame(objectName="taskLabel", margins=(0,0,0,0))  # taskObjectLabel is used to treat the frame like the other labels
                    taskLabel.layout().setSpacing(0)

                    # A frame, layout and placeholderlabel form the structure to hold the representative color 
                    colorFrame = createLayoutFrame(sizePolicy=("fixed", "fixed"), margins=(0,0,0,0)) # The frame that holds the actual color
                    colorFrame.setStyleSheet(f"background-color: {color};") # Color changes based on priority 
                    colorFrame.setFixedSize(20, 20)

                    priorityLabel = DataLabel(f'{priority}', feature, objectName="priorityLabel")
                    taskLabel.layout().addWidget(priorityLabel)                            
                    taskLabel.layout().addWidget(colorFrame)

                # Labels other than the priority
                else:
                    taskLabel = DataLabel(f'{value}', feature, objectName="taskLabel")
                        
                taskLabel.installEventFilter(self)
                taskLabel.mousePressEvent = (partial(self.rowClicked, feature["featureDescription"]))
                self.featureGrid.addWidget(taskLabel, feature["rowId"], self.featureHeaderColumnId[key])
                rowList.append(taskLabel)

        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, feature["featureDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList))  

            
    # ========================================================================================
    

    def rowClicked(self, featureDescription, event):   
        
        if event.button() == Qt.LeftButton:
            ic("rowClicked")
        

    # ========================================================================================

    def hoverEnter(self, labelRowList, featureDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(featureDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.qssController.hoverEnterStyle)


    # ========================================================================================
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.qssController.hoverLeaveStyle)


    # ========================================================================================
    
    
    def removeFeature(self, featureId):
        
        messageBox = QMessageBox()
        messageBox.setMinimumSize(200, 200)
        messageBox.setWindowTitle("Delete Feature?")
        messageBox.setText("Are you sure you want to delete this feature?")
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messageBox.setDefaultButton(QMessageBox.Cancel)
        ret = messageBox.exec()
        
        if ret == QMessageBox.Ok:
            # Remove task from the database
            self.parentView.viewController.model.deleteFeature(featureId)  

            # Clear and redisplay tasks in grid
            self.parentView.setActiveWindow(self.tabId)
            

    # ========================================================================================
            
    # Adding actions to the right-click context menu
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
            
            rightMenu = QMenu(self)
            
            # -- Edit Menu --
            editAction = createActionDictionary("Edit", trigger=partial(self.editFeature, obj.data))
            
            # -- Delete Menu --
            deleteAction = createActionDictionary("Delete", trigger=partial(self.removeFeature, obj.data["featureId"]))
            
            actionList = [editAction, "separator", deleteAction]
            addActionToMenu(rightMenu, actionList)

            #---------------

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)


    # ========================================================================================
    
    
    def editFeature(self, feature):
        ic("right click")
        
        self.parentView.viewController.displayView("AddNewView", self.parentView, self.tabId, feature, editing=True, newWindow=True)
      
        
    # ========================================================================================
