from icecream import ic

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QMessageBox, QMenu, QComboBox
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QAction
from functools import partial
from Helpers.DataLabel import DataLabel


class FeatureTabView(QWidget):

    def __init__(self, parentView, viewController, projectId, editing=False):
        super().__init__()
        
        self.parentView = parentView
        self.viewController = viewController
        self.projectId = projectId
        self.editing = editing

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        
        self.featureGrid = self.parentView.window.FeatureTabGridFrame.layout()
        self.parentView.window.FeatureTabGridFrame.layout().setAlignment(Qt.AlignTop)
        
        if self.editing:
            finishEditBtn = QPushButton("Finish Editing", objectName="finishEditBtn")
            finishEditBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.parentView.window.FinishEditFrame.layout().addWidget(finishEditBtn)
            finishEditBtn.clicked.connect(self.editFinished)
        
        
        self.loadGrids()
        

    # ----------------------------------------------------------------------------------------
        

    def loadGrids(self):
        ic("loadGrids")

        self.clearGrids()
        self.setUpFeatureGrid()

        # self.populateIssueData()
        

    # ----------------------------------------------------------------------------------------
        

    def clearGrids(self):
        ic("clearGrids")
        
        while self.featureGrid.count():
            item = self.featureGrid.takeAt(0)
            if item.widget():
                item.widget().deleteLater()      
                

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
            for header in self.featureViewHeaders:
                if key in self.featureViewHeaders:

                    if key == "priority":
                        priorityDict = self.parentView.getPriorityDict() #from ProjectFeatureTaskIssueView
                        priority, color = priorityDict[value]["Priority"], priorityDict[value]["Color"]
                    
                        # Display the priority along with a representative color
                        priorityLayout = QHBoxLayout()
                        priorityLayout.setContentsMargins(0,0,0,0)
                        priorityLayout.setSpacing(0)
                        taskObjectLabel = QFrame()
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

                        # The priority label
                        if self.editing:
                            priorityLabel = QComboBox()
                            # -- Drop Down Menu --
                            self.priorityDict = self.parentView.getPriorityDict() 
         
                            for priorityValue in self.priorityDict.values():
                                priorityLabel.addItem(priorityValue["Priority"])
            
                            priorityLabel.setCurrentIndex(2)
                            
                        else:
                            priorityLabel = DataLabel(f'{priority}', feature, objectName="priorityLabel")
                            priorityLabel.installEventFilter(self)
                        
                        priorityLayout.addWidget(priorityLabel)
                        priorityLayout.addWidget(colorMasterFrame)
                        
                    else:
                        taskObjectLabel = DataLabel(f'{value}', feature)
                        taskObjectLabel.installEventFilter(self)
                    
                    taskObjectLabel.setObjectName("taskObjectLabel")
                                
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
        
        self.viewController.displayAddNewFeatureView(self.projectId)

         
    # ----------------------------------------------------------------------------------------
    

    def rowClicked(self, featureDescription, event):   
        
        if event.button() == Qt.LeftButton:
            ic("rowClicked")
        

    # ----------------------------------------------------------------------------------------

    def hoverEnter(self, labelRowList, featureDescription, event):
        
        self.parentView.window.DescriptionTextLabel.setText(featureDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.parentView.window.DescriptionTextLabel.setText("")
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.backgroundNormalStyle)


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
            self.parentView.model.deleteFeature(self.projectId, featureId)  

            # Clear and redisplay tasks in grid
            self.viewController.displayProjectFeatureTaskIssueView(self.projectId, currentIndex=self.parentView.currentIndex)
            

    # ----------------------------------------------------------------------------------------
            

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

        self.parentView.featureEdit(feature["rowId"])


    # ----------------------------------------------------------------------------------------


    def editFinished(self):
        ic("editFinished")


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
