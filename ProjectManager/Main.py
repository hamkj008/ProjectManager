from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from MainFiles.ViewController import ViewController



# Entry point of the program
class Main:
    
    def __init__(self):
        self.app = QApplication([])
        self.app.setWindowIcon(QIcon("icons/ProjectManagerIcon.png"))
        self.viewController = ViewController(self)
        

    def main(self):
        self.viewController.main()
       


    def exit(self):
        self.viewController.closeDatabase()
        self.app.exit()



if __name__ == "__main__":
    
    main = Main()
    main.main()
    main.app.exec()   





