from icecream import ic
from PySide6.QtWidgets import QWidget, QStatusBar
from PySide6.QtCore import Qt
from UiViews.UiLogWindow import Ui_LogWindow



class LogView(QWidget):
    
    def __init__(self, logController):
        super().__init__()
        
        self.logController = logController

        self.window = Ui_LogWindow()
        self.window.setupUi(self)
        
        with open('QSS\LogStyle.qss', 'r') as file:
             stylesheet = file.read()

        self.setStyleSheet(stylesheet)
        

        self.window.TextGridFrame.layout().setAlignment(Qt.AlignTop)

        # statusbar
        self.logController.setStatusBar(QStatusBar(self))  




        
