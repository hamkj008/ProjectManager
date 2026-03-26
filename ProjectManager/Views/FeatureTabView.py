from icecream import ic
from functools import partial

from PySide6.QtWidgets import QSizePolicy, QWidget, QLabel, QGridLayout, QMenu, QCheckBox
from PySide6.QtCore import Qt, QEvent

from MainFiles.Mixins.Utility_Mixin import Interaction_Mixin
from MyHelperLibrary.Helpers.DataLabel import DataLabel
from MyHelperLibrary.Helpers.HelperMethods import createActionDictionary, addActionToMenu, createLayoutFrame, clearLayout, getCurrentFunction, createCustomChoiceDialog


# ========================================================================================

class FeatureTabView(QWidget, Interaction_Mixin):

    def __init__(self, parentView, tabId: int, editDict: dict=None):
        super().__init__()
        ic(__class__.__name__)
        
        self.parentView = parentView
        self.tabId      = tabId
        self.editDict   = editDict
        
        # -----------
        
        # Create a new grid layout because the parent will be cleared each time
        self.featureGrid = QGridLayout()
        self.featureGrid.setAlignment(Qt.AlignTop)
        self.setLayout(self.featureGrid)
        
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
        self.retriggerStrikethrough()

    # ========================================================================================

    def getModel(self):
        self.modelResults = self.parentView.viewController.model.getFeatures(self.parentView.viewController.stateController.projectId)

    # ========================================================================================

    def setupGrid(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        self.featureHeaderColumnId  = {}
        self.featureViewHeaders     = {"completed"              : "Completed",
                                        "featureName"           : "Feature Summary", 
                                        "dateFeatureCreated"    : "Date Created",
                                        "priority"              : "Priority"}

        for index, (key, value) in enumerate(self.featureViewHeaders.items()):
            columnTitle = QLabel(value, objectName="header")
            
            self.featureGrid.addWidget(columnTitle, 0, index)
            self.featureHeaderColumnId[key] = index
            
    # ========================================================================================

    def populateData(self):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        # -- Populate Data --
        for rowIndex, feature in enumerate(self.modelResults):
            
            feature["rowId"] = rowIndex + 1
                
            self.addFeatureToDisplay(feature)  
            
        statusBarMessage = "Features: " + str(len(self.modelResults))
        self.parentView.viewController.statusBar().showMessage(statusBarMessage)

    # ========================================================================================
    
    def addFeatureToDisplay(self, feature):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
                
        rowList = []

        # -- Complete Checkbox --
        completeCheckbox = QCheckBox(objectName="completeCheckbox")
        completeCheckbox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)      
        completeCheckbox.toggled.connect(partial(self.featureComplete, feature))

        # if feature["isComplete"] == 'True':
        #     completeCheckbox.setChecked(True)
        self.featureGrid.addWidget(completeCheckbox, feature["rowId"], self.featureHeaderColumnId["completed"], alignment=Qt.AlignCenter)
        
        for key, value in feature.items():              

            if key in self.featureViewHeaders:

                if key == "priority":
                    priority, color = self.priorityDict[value]["Priority"], self.priorityDict[value]["Color"]
                        
                    # Display the priority along with a representative color
                    taskLabel = createLayoutFrame(objectName="taskLabel", margins=(0,0,0,0))  # taskObjectLabel is used to treat the frame like the other labels
                    taskLabel.layout().setSpacing(0)

                    # A frame, layout and placeholderlabel form the structure to hold the representative color 
                    colorFrame = createLayoutFrame(sizePolicy=("fixed", "fixed"), margins=(0,0,0,0)) # The frame that holds the actual color
                    colorFrame.setStyleSheet(f"background-color: {color}; border-radius: 10px;") # Color changes based on priority 
                    colorFrame.setFixedSize(20, 20)

                    priorityLabel = DataLabel(f'{priority}', feature, objectName="priorityLabel")
                    taskLabel.layout().addWidget(priorityLabel)                            
                    taskLabel.layout().addWidget(colorFrame)

                # Labels other than the priority
                else:
                    taskLabel = DataLabel(f'{value}', feature, objectName="taskLabel")

                    if key == "featureName":
                        taskLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                    if key == "dateFeatureCreated":
                        taskLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                        
                taskLabel.installEventFilter(self)
                taskLabel.mousePressEvent = (partial(self.rowClicked, feature["featureDescription"]))
                self.featureGrid.addWidget(taskLabel, feature["rowId"], self.featureHeaderColumnId[key])
                rowList.append(taskLabel)

        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, self.parentView.window.DescriptionTextLabel, feature["featureDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList, self.parentView.window.DescriptionTextLabel))  

    # ========================================================================================
    
    def rowClicked(self, featureDescription, event):   
        
        if event.button() == Qt.LeftButton:
            ic("rowClicked")
        
    # ========================================================================================
    
    def removeFeature(self, featureId):
        if createCustomChoiceDialog("Delete Feature?", 
                                "Are you sure you want to delete this feature?", 400, 300, self.viewController.qssController.getDialogStyle()):

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
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        self.parentView.viewController.displayView("AddNewView", self.parentView, self.tabId, feature, editing=True, newWindow=True)
        
    # ========================================================================================

    # If the task has been marked for completion, a strikethrough will be marked on the text
    def featureComplete(self, feature, checked):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        priority, color = self.priorityDict[feature["priority"]]["Priority"], self.priorityDict[feature["priority"]]["Color"]
        frame           = self.featureGrid.itemAtPosition(feature["rowId"], self.featureHeaderColumnId["priority"]).widget()
        priorityLabel   = frame.findChild(DataLabel, "priorityLabel")

        if checked:
            # Update database
            self.parentView.viewController.model.updateCompleteFeature(feature["featureId"], True)

            # Add the strikethrough to the task            
            self.featureGrid.itemAtPosition(feature["rowId"], self.featureHeaderColumnId["featureName"]).widget().setText(f"<s>{feature['featureName']}</s>")
            self.featureGrid.itemAtPosition(feature["rowId"], self.featureHeaderColumnId["dateFeatureCreated"]).widget().setText(f"<s>{feature['dateFeatureCreated']}</s>")
            priorityLabel.setText(f"<s>{priority}</s>")

        else:
            # Update database
            self.parentView.viewController.model.updateCompleteFeature(feature["featureId"], False)
            
            # Unmark (remove strikethrough) the task
            self.featureGrid.itemAtPosition(feature["rowId"], self.featureHeaderColumnId["featureName"]).widget().setText(f"{feature['featureName']}")
            self.featureGrid.itemAtPosition(feature["rowId"], self.featureHeaderColumnId["dateFeatureCreated"]).widget().setText(f"{feature['dateFeatureCreated']}")
            priorityLabel.setText(f"{priority}")

    # =============================================================================================

    def retriggerStrikethrough(self):
        
        # Retrigger the strikethrough if the task has been marked completed so it displays properly in the area
        for feature in self.modelResults:
            
            if feature["featureCompleted"] == 'True':
                checkbox = self.featureGrid.itemAtPosition(feature["rowId"], self.featureHeaderColumnId["completed"]).widget()
                checkbox.setChecked(True)
                self.featureComplete(feature, True)

    # =============================================================================================