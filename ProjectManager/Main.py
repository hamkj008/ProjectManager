from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from MainFiles.ViewController import ViewController
import sys
from pathlib import Path


# Entry point of the program
class Main:
    
    def __init__(self):
        self.app = QApplication([])
        
        if getattr(sys, "frozen", False):           # If running as an executable
            programDirectory = Path(sys._MEIPASS)   # PyInstaller temp directory
        else:
            programDirectory = Path(__file__).resolve().parent

        iconPath = str(programDirectory / "icons/ProjectManagerIcon.png")
        self.app.setWindowIcon(QIcon(iconPath))
        self.viewController = ViewController(self, iconPath)
        

    def main(self):
        self.viewController.main()


    def exit(self):
        self.viewController.closeDatabase()
        self.app.exit()



if __name__ == "__main__":
    
    main = Main()
    main.main()
    main.app.exec()   





