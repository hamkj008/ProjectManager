from icecream import ic

from PySide6.QtWidgets import QLineEdit, QWidget, QLabel, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QMessageBox, QMenu, QComboBox
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QAction
from functools import partial
from Helpers.DataLabel import DataLabel


class FeatureTabView(QWidget):

    def __init__(self, parentView, tabId, editDict=None):
        super().__init__()
        
        self.parentView = parentView
        self.tabId = tabId
        self.editDict = editDict

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        
        self.featureGrid = self.parentView.window.FeatureTabGridFrame.layout()
        self.parentView.window.FeatureTabGridFrame.layout().setAlignment(Qt.AlignTop)
        
        self.priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
        

        # If an entry is being edited, add the finish button to the display
        if self.editDict and self.editDict["isEditing"]:
            finishEditBtn = QPushButton("Finish Editing", objectName="finishEditBtn")
            finishEditBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.parentView.window.FinishEditFrame.layout().addWidget(finishEditBtn)
            finishEditBtn.clicked.connect(self.editFinished)
        
        
        self.setUpFeatureGrid()
        

    # ----------------------------------------------------------------------------------------


    def setUpFeatureGrid(self):
        ic("setUpFeatureGrid")

        self.featureHeaderColumnId = {}
        self.featureViewHeaders = {"featureName"            : "Feature Summary", 
                                    "dateFeatureCreated"    : "Date Created",
                                    "priority"              : "Priority"}

        for index, (key, value) in enumerate(self.featureViewHeaders.items()):
            columnTitle = QLabel(value, objectName="header")
              
            self.featureGrid.addWidget(columnTitle, 0, index)
            self.featureHeaderColumnId[key] = index
   
            
    # ----------------------------------------------------------------------------------------


    def addFeatureToDisplay(self, feature):
        ic("addFeatureToDisplay")
                
        rowList = []
        
        for key, value in feature.items():           
            if key in self.featureViewHeaders:
                    
                if key == "priority":
                    priority, color = self.priorityDict[value]["Priority"], self.priorityDict[value]["Color"]
                        
                    # Display the priority along with a representative color
                    priorityLayout = QHBoxLayout()
                    priorityLayout.setContentsMargins(0,0,0,0)
                    priorityLayout.setSpacing(0)
                    taskObjectLabel = QFrame(objectName="taskObjectLabel")  # taskObjectLabel is used to treat the frame like the other labels
                    taskObjectLabel.setLayout(priorityLayout)
                        
                    # Used to control the size of the color frame
                    colorMasterFrame = QFrame()
                    colorMasterFrame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    colorMasterLayout = QHBoxLayout()
                    colorMasterLayout.setContentsMargins(0,0,0,0)
                    colorMasterFrame.setLayout(colorMasterLayout)
                    
                    # A frame, layout and placeholderlabel form the structure to hold the representative color 
                    colorFrame = QFrame() # The frame that holds the actual color
                    colorFrame.setStyleSheet(f"background-color: {color};") # Color changes based on priority 
                    colorFrame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)                   
                    colorFrameLayout = QHBoxLayout()
                    colorFrameLayout.setContentsMargins(0,0,0,0)
                    colorFrame.setLayout(colorFrameLayout)
                    placeholder = QLabel("", objectName="placeholder") # A placeholder to give the frame substance
                    placeholder.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    colorFrameLayout.addWidget(placeholder)
                    
                    colorMasterLayout.addWidget(colorFrame)
                    
                    # -- Editing --
                    if self.editDict and self.editDict["isEditing"] and feature["rowId"] == self.editDict["rowId"]:
                            
                        # -- Drop Down Menu --
                        self.prioritySelectionMenu = QComboBox()

                        for priorityValue in self.priorityDict.values():
                            self.prioritySelectionMenu.addItem(priorityValue["Priority"])
            
                        self.prioritySelectionMenu.setCurrentIndex(2) # Set a default selection
                        priorityLayout.addWidget(self.prioritySelectionMenu)
                            
                    # -- Not editing --
                    else:
                        priorityLabel = DataLabel(f'{priority}', feature, objectName="priorityLabel")
                        priorityLabel.installEventFilter(self) # Apply right click menu to labels
                        priorityLayout.addWidget(priorityLabel)                            
                        priorityLayout.addWidget(colorMasterFrame)
                        
                        rowList.append(taskObjectLabel)
                            
                    taskObjectLabel.mousePressEvent = (partial(self.rowClicked, feature["featureDescription"]))
                    self.featureGrid.addWidget(taskObjectLabel, feature["rowId"], self.featureHeaderColumnId[key])
               

                # Labels other than the priority
                else:
                    # -- Editing --
                    if self.editDict and self.editDict["isEditing"] and feature["rowId"] == self.editDict["rowId"] and key == "featureName":
                        self.featureNameInput = QLineEdit(f'{value}')  
                        self.featureGrid.addWidget(self.featureNameInput, feature["rowId"], self.featureHeaderColumnId[key])
                            
                    # -- Not editing --
                    else:
                        taskObjectLabel = DataLabel(f'{value}', feature, objectName="taskObjectLabel")
                        taskObjectLabel.installEventFilter(self)
                                
                        taskObjectLabel.mousePressEvent = (partial(self.rowClicked, feature["featureDescription"]))
                        self.featureGrid.addWidget(taskObjectLabel, feature["rowId"], self.featureHeaderColumnId[key])
               
                        rowList.append(taskObjectLabel)


        # If hovering for one label, all of them will highlight
        for widget in rowList:
            widget.enterEvent = (partial(self.hoverEnter, rowList, feature["featureDescription"]))
            widget.leaveEvent = (partial(self.hoverLeave, rowList))  

            
    # ----------------------------------------------------------------------------------------
    

    def addNewFeature(self):
        ic("addNewFeature")
        
        self.parentView.viewController.displayAddNewFeatureView(self.parentView.projectId)

         
    # ----------------------------------------------------------------------------------------
    

    def rowClicked(self, featureDescription, event):   
        
        if event.button() == Qt.LeftButton:
            ic("rowClicked")
        

    # ----------------------------------------------------------------------------------------

    def hoverEnter(self, labelRowList, featureDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(featureDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.parentView.viewController.backgroundNormalStyle)


    # ----------------------------------------------------------------------------------------
    
    
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
            self.parentView.model.deleteFeature(self.parentView.projectId, featureId)  

            # Clear and redisplay tasks in grid
            self.parentView.createFeatureTabView()
            

    # ----------------------------------------------------------------------------------------
            
    # Sets up the right click context menu
    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:
            ic("contextMenu")
            
            rightMenu = QMenu(self)

            # Adding actions to the context menu
            # -- Edit Menu --
            edit = QAction("Edit", self)
            edit.triggered.connect(partial(self.editFeature, obj.data))
            rightMenu.addAction(edit)
            
            rightMenu.addSeparator()

            #---------------
            
            # -- Delete Menu --
            delete = QAction("Delete", self)
            delete.triggered.connect(partial(self.removeFeature, obj.data["featureId"]))
            rightMenu.addAction(delete)

            # Show context menu
            rightMenu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)


    # ----------------------------------------------------------------------------------------
    
    
    def editFeature(self, feature):
        ic("right click")
        
        self.editDict = {"featureId": feature["featureId"], "rowId": feature["rowId"], "tabId": self.tabId, "isEditing": True}

        self.parentView.createFeatureTabView(self.editDict)


    # ----------------------------------------------------------------------------------------


    def editFinished(self):
        ic("editFinished")
        
        selection = 0

        for key, value in self.priorityDict.items():
            if self.prioritySelectionMenu.currentText() == value["Priority"]:
                selection = key
                break
            
        self.parentView.model.updateFeature(self.parentView.projectId, self.editDict["featureId"], self.featureNameInput.text(), selection)
        self.editDict["isEditing"] = False

        # Clear the finish edit button from the display
        self.parentView.clearLayout(self.parentView.window.FinishEditFrame.layout())
        
        # Clear and redisplay tasks in grid
        self.parentView.createFeatureTabView(self.editDict)
      
        
    # ----------------------------------------------------------------------------------------






    # ----------------------------------------------------------------------------------------
    
    
    def get_widgets_in_row(self, layout, row):
        widgets = []
        for col in range(layout.columnCount()):
            item = layout.itemAtPosition(row, col)
            if item:
                widget = item.widget()
                if widget:
                    widgets.append(widget)
        return widgets
    

    def findChildrenRecursive(self, widget):
        def findChildren(widget):
            if isinstance(widget, DataLabel):
                return widget  # Return the widget when found
            elif isinstance(widget, QWidget):
                for child in widget.findChildren(QWidget):
                    result = findChildren(child)  # Recursively search children
                    if result:
                        return result  # Propagate the result up the call stack

        return findChildren(widget)  # Call the inner function and return its result
