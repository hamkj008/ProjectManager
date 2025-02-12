from icecream import ic
from MyHelperLibrary.Helpers.HelperMethods import readJSONData


""" Stores the application wide states for various variables """
class StateController:
    def __init__(self):
        ic("state controller")

        self.configData = readJSONData("JSON/config.json")
        
        self._projectId = None       


    # ================================================
    

    @property
    def projectId(self):
        if self._projectId:
            return self._projectId
        else:
            ic("Tried to access None projectId")

    @projectId.setter
    def projectId(self, projectId):
        self._projectId = projectId
        

    # ================================================

            
    def getVersionNumber(self):        
        return self.configData["version"]
    
    
    # ================================================ 