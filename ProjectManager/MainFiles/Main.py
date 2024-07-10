from PySide6.QtWidgets import QApplication
from ViewController import ViewController
from LogController import LogController
from PySide6.QtCore import Qt
from icecream import ic

# Entry point of the program
class Main:
    
    def __init__(self):
        self.app = QApplication([])
        self.logController = LogController()
        self.viewController = ViewController(self, self.logController)
        

    def main(self):
        self.viewController.main()
        self.logController.main()
       


    def exit(self):
        self.viewController.closeDatabase()
        self.app.exit()



if __name__ == "__main__":
    
    main = Main()
    main.main()
    main.app.exec()   





