from icecream import ic
from functools import partial
from MyHelperLibrary.Helpers.HelperMethods import createMenu, createActionDictionary, getAction, replaceActionTriggeredConnection



class MenuController:
   
    def __init__(self, viewController):
        ic("MenuController init")
        
        self.viewController = viewController

        self.menuList = {}


    # ========================================================================================
    
    def setupMenus(self, menubar):

        actionList = []
        
        # ----- File Menu -----        
        newAction       =   createActionDictionary("New", shortcut="Ctrl+N")
        exitAction      =   createActionDictionary("Exit", shortcut="Ctrl+Q", trigger=self.viewController.Main.exit)
        actionList      =   [newAction, "separator", exitAction]
        
        self.menuList["fileMenu"] = createMenu(menubar, "File", actionList)


        # ----- Settings Menu -----
        openPreferencesAction   =   createActionDictionary("Preferences", shortcut="Ctrl+P")
        actionList              =   [openPreferencesAction]
        
        self.menuList["settingsMenu"] = createMenu(menubar, "Settings", actionList)


        # ----- About Menu -----
        readmeAction    =   createActionDictionary("View README")
        aboutAction     =   createActionDictionary("About", trigger=partial(self.viewController.displayView, "AboutView", newWindow=True))
        actionList      =   [readmeAction, "separator", aboutAction]
        
        self.menuList["helpMenu"] = createMenu(menubar, "Help", actionList)
        
        
    # ========================================================================================
    

    def refreshContextMenus(self):
        ic("refreshContextMenus")



    # ========================================================================================
