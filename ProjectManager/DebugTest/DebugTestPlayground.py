from icecream import ic
from DebugTest.DebugTestSetup import DebugTestSetup
from MyHelperLibrary.Helpers.HelperMethods import createDictionary


class DebugTestPlayground:
   
    def __init__(self):
        
        self.debugtestsetup = DebugTestSetup()
        self.debugtestsetup.setupDB()
        self.populateData = self.debugtestsetup.populateDatabase()
        
        self.initTest(self.populateData)


    def initTest(self, populateDatabase):
        ic("initTest")
        
        feature = self.projectModel.getFeature(populateDatabase["feature"]["featureId"])
        ic(feature)
