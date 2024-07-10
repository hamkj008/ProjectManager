import datetime

from UiViews.UiAddNewProjectWindow import Ui_AddNewProjectWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt


class AddNewProjectView(QMainWindow):
    

    def __init__(self, viewController):
        super().__init__()
        self.viewController = viewController

        self.window = Ui_AddNewProjectWindow()
        self.window.setupUi(self)
        self.setWindowTitle("New Project")
        
        with open('QSS\AddTaskStyle.qss', 'r') as file:
             stylesheet = file.read()

        self.setStyleSheet(stylesheet)

        self.window.ProjectDescriptionTextEdit.setAlignment(Qt.AlignTop)
        self.window.ProjectDescriptionLabel.setAlignment(Qt.AlignTop)

        # -- Signals --
        self.window.AddNewProjectBtn.clicked.connect(self.getProjectInfo)


    # ----------------------------------------------------------------------------------------
    

    def main(self):
        self.show()
        
    # ----------------------------------------------------------------------------------------
    

    def getProjectInfo(self):
        
        # Retrieve the data from the form, arrange it into a dictionary, then send it back to the controller
        projectName = self.window.ProjectNameInputField.text()
        projectDescription = self.window.ProjectDescriptionTextEdit.toPlainText()
        dateCreated = datetime.datetime.now().date().strftime("%Y-%m-%d")
        
        if len(projectName) > 0:
            projectInfoDict = {"projectName": projectName, 
                                "projectDescription": projectDescription,
                                "dateCreated": dateCreated}
        
            self.viewController.addNewProject(projectInfoDict)

        else:
            self.displayEmptyFieldsMessageBox()
            

    
    def displayEmptyFieldsMessageBox(self):
        
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Empty project details")
        messageBox.setText("Enter the project details")
        messageBox.addButton(QMessageBox.Ok)
        messageBox.exec()