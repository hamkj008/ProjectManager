from icecream import ic

from PySide6.QtWidgets import QWidget
from UiViews.UiPreferencesView import Ui_MainWidget
from MyHelperLibrary.Helpers.CustomWindow import CustomWindow
from MainFiles.QSSController import Theme



class PreferencesView(CustomWindow):

    def __init__(self, viewController, qssController):
        super().__init__("Preferences", "", False)

        self.viewController = viewController
        self.qssController  = qssController

        self.setWindowTitle("Preferences")
        
        # The primary widget to host the ui content 
        self.container  = QWidget()
        self.setCentralWidget(self.container)

        self.content = Ui_MainWidget()
        self.content.setupUi(self.container)

        # ---- Style ----
        self.setStyle()
        # --------------

        for option in Theme:
            self.content.themeOptionsComboBox.addItem(option.name)

        self.content.themeOptionsComboBox.adjustSize()     # Ensures that the combo box’s size is updated to accommodate the contents of its items
        self.content.themeOptionsComboBox.setCurrentIndex((Theme(self.qssController.currentTheme).value) -1)
        self.content.themeOptionsComboBox.currentIndexChanged.connect(self.changeTheme)
        


    # =============================================================================================


    def setStyle(self):

        stylesheet = self.qssController.getStandardStyle()
        # stylesheet += self.qssController.getContentStyle()
        # stylesheet += f"#MainWidget {{ border-bottom: 2px solid {self.qssController.borderColor}; }} #themeOptionsLabel {{ color: {self.qssController.titleBarText}; }} "
        self.setStyleSheet(stylesheet)


    # =============================================================================================


    def main(self):
        self.show()

        
    # =============================================================================================


    def changeTheme(self, value):

        self.qssController.setTheme(Theme(value + 1))
        self.setStyle()
        self.viewController.setStyle()        
