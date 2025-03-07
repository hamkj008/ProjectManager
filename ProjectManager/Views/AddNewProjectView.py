import datetime

from UiViews.UiAddNewProjectWindow import Ui_AddNewProjectWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap

from MyHelperLibrary.Helpers.HelperMethods import createCustomDialog, showError, clearError


# ========================================================================================
      

class AddNewProjectView(QMainWindow):
    

    def __init__(self, viewController, projectDict, editing):
        super().__init__()
        self.viewController = viewController
        self.projectDict = projectDict
        self.editing = editing

        # ------- Setup UI --------
        
        self.window = Ui_AddNewProjectWindow()
        self.window.setupUi(self)
        self.setStyle()
        
        # --------------------------

        self.setWindowIcon(QIcon("icons/ProjectManagerIcon.png"))

        self.window.DescriptionTextEdit.setAlignment(Qt.AlignTop)
        self.window.DescriptionLabel.setAlignment(Qt.AlignTop)
        
        self.errorFrames = {"nameErrorFrame" : self.window.NameInputErrorFrame}
        self.errorFrames["nameErrorFrame"].setVisible(False)

        # -- Signals --
        self.window.AddNewBtn.clicked.connect(self.getProjectInfo)

        self.isEditing(projectDict, editing)
        
        
    # ========================================================================================
    

    def main(self):
        self.show()
        

    # ========================================================================================
    

    def setStyle(self):
        
        styleSheet = self.viewController.qssController.getStandardStyle()
        styleSheet += self.viewController.qssController.getAddStyle()
        self.setStyleSheet(styleSheet)


    # ========================================================================================
    

    def isEditing(self, projectDict, editing):
        
        if editing:
            
            # Change labels for different window
            self.setWindowTitle(f"Edit Project")
            self.window.AddNewBtn.setText(f"Update Project")

            self.window.NameInput.setText(projectDict["projectName"]), 
            self.window.DescriptionTextEdit.setText(projectDict["projectDescription"])         
                
        else:
            self.setWindowTitle(f"New Project")
            self.window.AddNewBtn.setText(f"Add Project")


    # ========================================================================================
    

    def getProjectInfo(self):
        
        # clear any invalid format errors previously left
        clearError(self.errorFrames)
        
        # Retrieve the data from the form, arrange it into a dictionary, then send it back to the controller
        projectName         = self.window.NameInput.text()
        projectDescription  = self.window.DescriptionTextEdit.toPlainText()
        dateCreated         = datetime.datetime.now().date().strftime("%Y-%m-%d")
        
        if len(projectName) > 0:
            projectInfoDict = {"projectName"            :   projectName, 
                                "projectDescription"    :   projectDescription,
                                "dateCreated"           :   dateCreated}
        
            if self.editing:
                projectInfoDict["projectId"] = self.projectDict["projectId"]
                self.viewController.model.updateProject(projectInfoDict)
            else:
                self.viewController.model.addNewProject(projectInfoDict)
                
            self.viewController.closeView("AddNewProjectView")
            self.viewController.displayView("ProjectView")
            
        else:
            showError(self.errorFrames["nameErrorFrame"])
            createCustomDialog("Empty project details", "Enter the project details", 300, 300, self.viewController.qssController.getDialogStyle())
            

    # ========================================================================================