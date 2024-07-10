import datetime

from UiViews.UiAddNewTaskWindow import Ui_AddNewTaskWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt


class AddNewFeatureView(QMainWindow):
    

    def __init__(self, viewController, parentView, projectId):
        super().__init__()
        
        self.viewController = viewController
        self.parentView = parentView
        self.projectId = projectId

        self.window = Ui_AddNewTaskWindow()
        self.window.setupUi(self)
        self.setWindowTitle("New Feature")
        
        with open('QSS\AddTaskStyle.qss', 'r') as file:
             stylesheet = file.read()

        self.setStyleSheet(stylesheet)

        self.window.TaskDescriptionTextEdit.setAlignment(Qt.AlignTop)
        self.window.TaskDescriptionLabel.setAlignment(Qt.AlignTop)

        # -- Signals --
        self.window.AddTaskBtn.setText("Add Feature")
        self.window.AddTaskBtn.clicked.connect(self.getFeatureInfo)


        # -- Drop Down Menu --
        self.priorityDict = self.parentView.getPriorityDict() 
         
        for value in self.priorityDict.values():
            self.window.PriorityComboBox.addItem(value["Priority"])

        self.window.PriorityComboBox.setCurrentIndex(2)
        

    # ----------------------------------------------------------------------------------------
    

    def main(self):
        self.show()
        
    # ----------------------------------------------------------------------------------------
    

    def getFeatureInfo(self):
        
        # Retrieve the data from the form, arrange it into a dictionary, then send it back to the controller
        featureName = self.window.TaskNameInputField.text()
        featureDescription = self.window.TaskDescriptionTextEdit.toPlainText()
        dateFeatureCreated = datetime.datetime.now().date().strftime("%Y-%m-%d")
        priority = self.window.PriorityComboBox.currentText()
        
        if len(featureName) > 0:
            for key, value in self.priorityDict.items():
                if value["Priority"] == priority:
                    priorityKey = key
                
            featureInfoDict = {"featureName"            :   featureName, 
                                "projectId"             :   self.projectId,
                                "featureDescription"    :   featureDescription,
                                "dateFeatureCreated"    :   dateFeatureCreated,
                                "priority"              :   priorityKey}
        
            self.viewController.addNewFeature(featureInfoDict)


        else:
            self.displayEmptyFieldsMessageBox()
            

    # ----------------------------------------------------------------------------------------
    
    
    def displayEmptyFieldsMessageBox(self):
        
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Empty feature details")
        messageBox.setText("Enter the feature details")
        messageBox.addButton(QMessageBox.Ok)
        messageBox.exec()
