from icecream import ic
from functools import partial
from MyHelperLibrary.Helpers.HelperMethods import createMenu, createActionDictionary



class MenuController:
   
    def __init__(self, viewController):
        ic("MenuController init")
        
        self.viewController = viewController
        self.menuList       = {}


    # ========================================================================================
    
    def setupMenus(self, menubar):

        actionList = []
        
        # ----- File Menu -----        
        newAction       =   createActionDictionary("New", shortcut="Ctrl+N", trigger=self.getNew)
        exitAction      =   createActionDictionary("Exit", shortcut="Ctrl+Q", trigger=self.viewController.Main.exit)
        actionList      =   [newAction, "separator", exitAction]
        
        self.menuList["fileMenu"] = createMenu(menubar, "File", actionList)


        # ----- Settings Menu -----
        openPreferencesAction   =   createActionDictionary("Preferences", shortcut="Ctrl+P", trigger=partial(self.viewController.displayView, "PreferencesView", newWindow=True))
        actionList              =   [openPreferencesAction]
        
        self.menuList["settingsMenu"] = createMenu(menubar, "Settings", actionList)


        # ----- About Menu -----
        aboutAction     =   createActionDictionary("About", trigger=partial(self.viewController.displayView, "AboutView", newWindow=True))
        actionList      =   [aboutAction]
        
        self.menuList["helpMenu"] = createMenu(menubar, "Help", actionList)
        
        
    # ========================================================================================
    

    def refreshContextMenus(self):
        ic("refreshContextMenus")



    # ========================================================================================

    # Quick and dirty way of calling a common method on different classes
    def getNew(self):

        for view in list(self.viewController.viewList.values()):
            if view:
                if hasattr(view, "addNew"):
                    getattr(view, "addNew")()