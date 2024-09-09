from icecream import ic

from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QColorDialog
from PySide6.QtCore import Qt
from UiViews.UiAboutWindow import Ui_AboutWindow
from MyHelperLibrary.Helpers.HelperMethods import createTwoWayDictionary, createWidget, createLayoutFrame



class AboutView(QMainWindow):

    def __init__(self, viewController, versionNumber):
        super().__init__()
        self.viewController = viewController
        

        # ----- Setup UI -----
        self.window = Ui_AboutWindow()
        self.window.setupUi(self)
        self.setWindowTitle("About")
        self.setStyle()
        # --------------------
        
        # Create a drop shadow effect with a black color and offset
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setColor(Qt.black)
        shadow.setOffset(2, 2)  # Adjust the offset for the outline effect
    
        self.window.AboutTitleLabel.setGraphicsEffect(shadow)
        
        # -------------------------
        
        self.window.VersionDataLabel.setText(versionNumber)
        
        self.window.CloseBtn.clicked.connect(self.close)

    # ========================================================================================
            

    def main(self):
        self.show()


    # ======================================================================================== 
    

    def setStyle(self):
        
        stylesheet = self.viewController.qssController.getStandardStyle()
        self.setStyleSheet(stylesheet)


    # ========================================================================================
    

    def closeView(self):
        
        self.viewController.closeView("AboutView")
