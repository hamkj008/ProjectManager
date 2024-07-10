import datetime
from icecream import ic

from UiViews.UiAddNewTaskWindow import Ui_AddNewTaskWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt


class AddNewTaskView(QMainWindow):
    

    def __init__(self, viewController, parentView, projectId):
        super().__init__()

        self.viewController = viewController
        self.parentView = parentView
        self.projectId = projectId

        self.window = Ui_AddNewTaskWindow()
        self.window.setupUi(self)
        self.setWindowTitle("New Task")
        
        with open('QSS\AddTaskStyle.qss', 'r') as file:
            stylesheet = file.read()

        self.setStyleSheet(stylesheet)

        self.window.TaskDescriptionTextEdit.setAlignment(Qt.AlignTop)
        self.window.TaskDescriptionLabel.setAlignment(Qt.AlignTop)

        # -- Signals --
        self.window.AddTaskBtn.clicked.connect(self.getTaskInfo)


        # -- Drop Down Menu --
        self.priorityDict = parentView.getPriorityDict() 
         
        for value in self.priorityDict.values():
            self.window.PriorityComboBox.addItem(value["Priority"])
            
        self.window.PriorityComboBox.setCurrentIndex(2)

    # ----------------------------------------------------------------------------------------
    

    def main(self):
        self.show()
        
    # ----------------------------------------------------------------------------------------
    

    def getTaskInfo(self):
        
        # Retrieve the data from the form, arrange it into a dictionary, then send it back to the controller
        taskName = self.window.TaskNameInputField.text()
        taskDescription = self.window.TaskDescriptionTextEdit.toPlainText()
        dateTaskCreated = datetime.datetime.now().date().strftime("%Y-%m-%d")
        priority = self.window.PriorityComboBox.currentText()
        
        if len(taskName) > 0:
            
            for key, value in self.priorityDict.items():
                if value["Priority"] == priority:
                    priorityKey = key
        
            taskInfoDict = {"taskName"          : taskName, 
                            "projectId"         : self.projectId,
                            "taskDescription"   : taskDescription,
                            "dateTaskCreated"   : dateTaskCreated,
                            "priority"          : priorityKey}
        
            self.viewController.addNewTask(taskInfoDict)
        
        else:
            self.displayEmptyFieldsMessageBox()
            

    # ----------------------------------------------------------------------------------------
    
    
    def displayEmptyFieldsMessageBox(self):
        
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Empty task details")
        messageBox.setText("Enter the task details")
        messageBox.addButton(QMessageBox.Ok)
        messageBox.exec()