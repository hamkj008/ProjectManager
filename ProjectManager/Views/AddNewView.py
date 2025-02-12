from icecream import ic
import datetime

from UiViews.UiAddNewWindow import Ui_AddNewWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from MyHelperLibrary.Helpers.HelperMethods import createCustomDialog, showError, clearError


# ========================================================================================
      

class AddNewView(QMainWindow):
    

    def __init__(self, viewController, parentView, index, objectDict=None, editing=False):
        super().__init__()
        
        self.viewController = viewController
        self.parentView = parentView
        self.index = index
        self.objectDict = objectDict
        self.editing = editing

        # ----- Setup UI ---------
        self.window = Ui_AddNewWindow()
        self.window.setupUi(self)
        self.setStyle()
        # ------------------------

        self.setWindowIcon(QIcon("icons/ProjectManagerIcon.png"))

        self.window.DescriptionTextEdit.setAlignment(Qt.AlignTop)
        self.window.DescriptionLabel.setAlignment(Qt.AlignTop)
        
        self.errorFrames = {"nameErrorFrame" : self.window.NameInputErrorFrame}
        self.errorFrames["nameErrorFrame"].setVisible(False)
        
        # -- Configure --
        self.confDict = {"title"        : {0: "Feature",                1: "Task",             2: "Issue"},
                        "dialog"        : {0: "feature",                1: "task",             2: "issue"},
                        "name"          : {0: "featureName",            1: "taskName",         2: "issueName"},
                        "description"   : {0: "featureDescription",     1: "taskDescription",  2: "issueDescription"},
                        "dateCreated"   : {0: "dateFeatureCreated",     1: "dateTaskCreated",  2: "dateIssueCreated"}}


        # -- Signals --
        self.window.AddNewBtn.clicked.connect(self.getInfo)


        # -- Drop Down Menu --
        self.priorityDict = self.parentView.getPriorityDict() 
         
        for value in self.priorityDict.values():
            self.window.PriorityComboBox.addItem(value["Priority"])

        self.window.PriorityComboBox.setCurrentIndex(2)
        

        # --- Editing ---
        self.isEditing(objectDict, editing)

    # ========================================================================================
    

    def main(self):
        self.show()
        

    # ========================================================================================
    

    def setStyle(self):
        
        styleSheet = self.viewController.qssController.getStandardStyle()
        styleSheet += self.viewController.qssController.getAddStyle()
        self.setStyleSheet(styleSheet)


    # ========================================================================================
    
    def isEditing(self, objectDict, editing):
        
        if editing:
            
            # Change labels for different window
            self.setWindowTitle(f"Edit {self.confDict['name'][self.index]}")
            self.window.AddNewBtn.setText(f"Update {self.confDict['title'][self.index]}")

            self.window.NameInput.setText(objectDict[self.confDict['name'][self.index]]), 
            self.window.DescriptionTextEdit.setText(objectDict[self.confDict['description'][self.index]])
            self.window.PriorityComboBox.setCurrentIndex(objectDict["priority"])           
                
        else:
            self.setWindowTitle(f"New {self.confDict['title'][self.index]}")
            self.window.AddNewBtn.setText(f"Add {self.confDict['title'][self.index]}")


    # ========================================================================================
    

    def getInfo(self):
        
        # clear any invalid format errors previously left
        clearError(self.errorFrames)
        
        # Retrieve the data from the form, arrange it into a dictionary, then send it back to the controller
        name            =   self.window.NameInput.text()
        description     =   self.window.DescriptionTextEdit.toPlainText()
        dateCreated     =   datetime.datetime.now().date().strftime("%Y-%m-%d")
        priority        =   self.window.PriorityComboBox.currentText()
        
        # -- Validation --        
        if len(name) > 0:
            for key, value in self.priorityDict.items():
                if value["Priority"] == priority:
                    priorityKey = key
                
            # Create the dictionary based on which type of data is being added: features, tasks, issues
            infoDict = {"projectId"                                 :   self.viewController.stateController.projectId,
                        self.confDict["name"][self.index]           :   name,
                        self.confDict["description"][self.index]    :   description,
                        self.confDict["dateCreated"][self.index]    :   dateCreated,
                        "priority"                                  :   priorityKey}
            
            # --------------------------------------------
            
            if self.index == 0:
                if self.editing:
                    featureId = self.objectDict[f"{self.confDict['dialog'][self.index]}Id"]
                    infoDict["featureId"] = featureId
                    self.viewController.model.updateFeature(infoDict)                   
                else:
                    self.viewController.model.addNewFeature(infoDict)
                
            elif self.index == 1:
                if self.editing:
                    taskId = self.objectDict[f"{self.confDict['dialog'][self.index]}Id"]
                    infoDict["taskId"] = taskId
                    self.viewController.model.updateTask(infoDict)                   
                else:
                    self.viewController.model.addNewTask(infoDict)
                
            elif self.index == 2:
                if self.editing:
                    issueId = self.objectDict[f"{self.confDict['dialog'][self.index]}Id"]
                    infoDict["issueId"] = issueId
                    self.viewController.model.updateIssue(infoDict)                        
                else:
                    self.viewController.model.addNewIssue(infoDict)
            

            self.viewController.closeView("AddNewView")
            self.viewController.displayView("ProjectFeatureTaskIssueView", currentIndex=self.index)
            
        else:
            showError(self.errorFrames["nameErrorFrame"])
            createCustomDialog(f"Empty {self.confDict['dialog'][self.index]} details", f"Enter the {self.confDict['dialog'][self.index]} details", 300, 300, self.viewController.qssController.getDialogStyle())
            

    # ========================================================================================

