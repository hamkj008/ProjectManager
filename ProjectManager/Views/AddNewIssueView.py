import datetime

from UiViews.UiAddNewTaskWindow import Ui_AddNewTaskWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt


class AddNewIssueView(QMainWindow):
    

    def __init__(self, viewController, parentView, projectId):
        super().__init__()
        
        self.viewController = viewController
        self.parentView = parentView
        self.projectId = projectId

        self.window = Ui_AddNewTaskWindow()
        self.window.setupUi(self)
        self.setWindowTitle("New Issue")
        
        with open('QSS\AddTaskStyle.qss', 'r') as file:
            stylesheet = file.read()

        self.setStyleSheet(stylesheet)

        self.window.TaskDescriptionTextEdit.setAlignment(Qt.AlignTop)
        self.window.TaskDescriptionLabel.setAlignment(Qt.AlignTop)

        # -- Signals --
        self.window.AddTaskBtn.setText("Add Issue")
        self.window.AddTaskBtn.clicked.connect(self.getIssueInfo)
        
        # -- Drop Down Menu --
        self.priorityDict = self.parentView.getPriorityDict() 
         
        for value in self.priorityDict.values():
            self.window.PriorityComboBox.addItem(value["Priority"])

        self.window.PriorityComboBox.setCurrentIndex(2)

    # ----------------------------------------------------------------------------------------
    

    def main(self):
        self.show()
        
    # ----------------------------------------------------------------------------------------
    

    def getIssueInfo(self):
        
        # Retrieve the data from the form, arrange it into a dictionary, then send it back to the controller
        issueName = self.window.TaskNameInputField.text()
        issueDescription = self.window.TaskDescriptionTextEdit.toPlainText()
        dateIssueCreated = datetime.datetime.now().date().strftime("%Y-%m-%d")
        priority = self.window.PriorityComboBox.currentText()
        
        if len(issueName) > 0:
            
            for key, value in self.priorityDict.items():
                if value["Priority"] == priority:
                    priorityKey = key
        
            issueInfoDict = {"issueName"        : issueName, 
                            "projectId"         : self.projectId,
                            "issueDescription"  : issueDescription,
                            "dateIssueCreated"  : dateIssueCreated,
                            "priority"          : priorityKey}
        
            self.viewController.addNewIssue(issueInfoDict)


        else:
            self.displayEmptyFieldsMessageBox()
            

    # ----------------------------------------------------------------------------------------
    
    
    def displayEmptyFieldsMessageBox(self):
        
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Empty issue details")
        messageBox.setText("Enter the issue details")
        messageBox.addButton(QMessageBox.Ok)
        messageBox.exec()
