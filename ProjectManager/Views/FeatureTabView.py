from icecream import ic

from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QAction
from functools import partial


class FeatureTabView(QWidget):

    def __init__(self, parentView, window, viewController, projectId, model):
        super().__init__()
        
        self.parentView = parentView
        self.window = window
        self.viewController = viewController
        self.projectId = projectId
        self.model = model

        layout = QHBoxLayout(self)
        self.setLayout(layout)
        
        self.featureGrid = self.window.FeatureTabGridFrame.layout()
        self.window.FeatureTabGridFrame.layout().setAlignment(Qt.AlignTop)
        

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
                                    "priority"              : "Priority",
                                    "delete"                : ""}

        for index, (key, value) in enumerate(self.featureViewHeaders.items()):
            columnTitle = QLabel(value)
            columnTitle.setObjectName("header")
              
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
                        priorityLabel = QLabel(f'{priority}')
                        priorityLabel.setObjectName("taskObjectLabel")
                        layout.addWidget(priorityLabel)
                        layout.addWidget(colorMasterFrame)

                    else:
                        taskObjectLabel = QLabel(f'{value}')
                        taskObjectLabel.installEventFilter(self)
                    
                    taskObjectLabel.setObjectName("taskObjectLabel")
                                
                    taskObjectLabel.mousePressEvent = (partial(self.rowClicked, feature["featureDescription"]))
                    self.featureGrid.layout().addWidget(taskObjectLabel, feature["rowId"], self.featureHeaderColumnId[key])
               
                    rowList.append(taskObjectLabel)
                    
                else:
                    if header == "delete":
                        removeBtn = QPushButton("x")    
                        removeBtn.setObjectName("removeBtn")
                        removeBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                        removeBtn.clicked.connect(partial(self.removeFeature, feature["featureId"]))
                        self.featureGrid.layout().addWidget(removeBtn, feature["rowId"], self.featureHeaderColumnId[header])            
                
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
        
        self.window.DescriptionTextLabel.setText(featureDescription)
        
        for label in labelRowList:
            label.setStyleSheet(self.viewController.hoverEnterStyle)


    # ----------------------------------------------------------------------------------------
       

    def hoverLeave(self, labelRowList, event): 
        
        self.window.DescriptionTextLabel.setText("")
        
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
            self.model.deleteFeature(self.projectId, featureId)  

            # Clear and redisplay tasks in grid
            self.viewController.displayProjectFeatureTaskIssueView(self.projectId, currentIndex=self.parentView.currentIndex)
            

    # ----------------------------------------------------------------------------------------
            

    def eventFilter(self, obj, event):

        if event.type() == QEvent.ContextMenu:

            ic("contextMenu")
            context_menu = QMenu(self)

            # Adding actions to the context menu
            action1 = QAction("Action 1", self)
            action1.triggered.connect(self.rightMenuAction1)
            context_menu.addAction(action1)

            action2 = QAction("Action 2", self)
            action2.triggered.connect(self.rightMenuAction2)
            context_menu.addAction(action2)

            # Show context menu
            context_menu.exec(event.globalPos())
            
            return True
        
        return super().eventFilter(obj, event)

    # ----------------------------------------------------------------------------------------
    
    
    def rightMenuAction1(self):
        print("Action 1 triggered")

    def rightMenuAction2(self):
        print("Action 2 triggered")
