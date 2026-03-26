from icecream import ic
import sqlite3
from MyHelperLibrary.Helpers.HelperMethods import createDictionaryList, createSingleRecordDictionary, getCurrentFunction

# ========================================================================================

class ProjectModel:

    def __init__(self, viewController, connection=None):
        ic(__class__.__name__)
        
        self.viewController = viewController
        self.connection     = connection
        self.cursor         = self.connection.cursor()

    # ========================================================================================

    def getProjectName(self, projectId: int) -> str:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query   = "SELECT projectName FROM projects WHERE projectId = (?)"
        params  = [projectId]
        row     = self.cursor.execute(query, params).fetchone()
        
        return row[0] if row else None
    
    # ========================================================================================
    
    def getProjects(self, search: str=None) -> list:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = "SELECT projectId, projectName, projectDescription, dateCreated FROM projects"
        
        if search:
            query += " WHERE projectName LIKE (?)"
            params = [f"%{search}%"]
            self.cursor.execute(query, params)
            
        else:
            self.cursor.execute(query)
        
        rows = self.cursor.fetchall()
        return createDictionaryList(rows, self.cursor.description)
    
    # ========================================================================================      
    
    def getProject(self, projectId):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query  = """SELECT projectId, projectName, projectDescription, dateCreated 
                        FROM projects WHERE projectId = (?)"""
                        
        params = [projectId]
        record = self.cursor.execute(query, params).fetchone()

        return createSingleRecordDictionary(record, self.cursor.description)
    
    # ========================================================================================      
    
    def addNewProject(self, projectInfo: dict) -> int:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        params = [projectInfo["projectName"],
                projectInfo["projectDescription"],
                projectInfo["dateCreated"]]
        
        query  = "INSERT INTO projects (projectName, projectDescription, dateCreated) VALUES (?,?,?)"
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
            self.cursor.execute("SELECT projectId FROM projects WHERE projectId = LAST_INSERT_ROWID()")
            return self.cursor.fetchone()[0]

        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================   
    
    def updateProject(self, projectDict: dict):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query  = "UPDATE projects SET projectName = ?, projectDescription = ? WHERE projectId = ?"
        params = [projectDict["projectName"], 
                projectDict["projectDescription"], 
                projectDict["projectId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
            
    # ========================================================================================   
    
    def getFeatures(self, projectId: int, search: str=None) -> list:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = """SELECT projectId, featureId, featureName, featureDescription, 
                        dateFeatureCreated, priority, featureCompleted
                        FROM projectFeatures WHERE projectId = (?)"""
        
        params = [projectId]
        
        if search:
            query += f" AND featureName LIKE ?"        
            params.append(f"%{search}%")
            
        query += f" ORDER BY priority" 
        
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        return createDictionaryList(rows, self.cursor.description)
    
    # ========================================================================================
    
    def getFeature(self, featureId: int) -> dict:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = """SELECT projectId, featureId, featureName, featureDescription, 
                            dateFeatureCreated, priority, featureCompleted 
                            FROM projectFeatures WHERE featureId = (?)"""
        
        params = [featureId]
        
        record = self.cursor.execute(query, params).fetchone()
        return createSingleRecordDictionary(record, self.cursor.description)
    
    # ========================================================================================
    
    def addNewFeature(self, featureInfo: dict) -> int:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query = """INSERT INTO projectFeatures (projectId, featureName, featureDescription, 
                                            dateFeatureCreated, priority) 
                                            VALUES (?,?,?,?,?)"""
                                            
        params = [featureInfo["projectId"],
                featureInfo["featureName"],
                featureInfo["featureDescription"],
                featureInfo["dateFeatureCreated"],
                featureInfo["priority"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
            self.cursor.execute("SELECT featureId FROM projectFeatures WHERE featureId = LAST_INSERT_ROWID()")
            return self.cursor.fetchone()[0]
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================   
    
    def getTasks(self, projectId: int, search: str=None) -> list:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = """SELECT projectId, taskId, taskName, taskDescription, dateTaskCreated, 
                    taskStatus, priority, isComplete 
                    FROM projectTasks WHERE projectId = (?)"""
                    
        params = [projectId]
        
        if search:
            query += f" AND taskName LIKE ?"            
            params.append(f"%{search}%")
            
        query += f" ORDER BY priority"    
        rows = self.cursor.execute(query, params).fetchall()

        return createDictionaryList(rows, self.cursor.description)
    
    # ========================================================================================
    
    def getTask(self, taskId: int) -> dict:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = """SELECT projectId, taskId, taskName, taskDescription, dateTaskCreated, 
                    taskStatus, priority, isComplete 
                    FROM projectTasks WHERE taskId = (?)"""
                    
        params = [taskId]
        record = self.cursor.execute(query, params).fetchone() 

        return createSingleRecordDictionary(record, self.cursor.description)
    
    # ========================================================================================
    
    def addNewTask(self, taskInfo: dict) -> int:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query = """INSERT INTO projectTasks (projectId, taskName, taskDescription, 
                                            dateTaskCreated, priority) 
                                            VALUES (?,?,?,?,?)"""
                                            
        params = [taskInfo["projectId"],
                taskInfo["taskName"],
                taskInfo["taskDescription"],
                taskInfo["dateTaskCreated"],
                taskInfo["priority"]]    
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
            self.cursor.execute("SELECT taskId FROM projectTasks WHERE taskId = LAST_INSERT_ROWID()")
            return self.cursor.fetchone()[0]
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================   
    
    def getIssues(self, projectId: int, search: str=None) -> list:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = """SELECT projectId, issueId, issueName, issueDescription, 
                    dateIssueCreated, isComplete, priority 
                    FROM projectIssues WHERE projectId = (?)"""
                    
        params = [projectId]
        
        if search:
            query += f" AND issueName LIKE ?"
            params.append(f"%{search}%")
        
        query += f" ORDER BY priority"
        rows = self.cursor.execute(query, params).fetchall()

        return createDictionaryList(rows, self.cursor.description)
    
    # ========================================================================================
    
    def getIssue(self, issueId: int) -> dict:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -
        
        query = """SELECT projectId, issueId, issueName, issueDescription, 
                            dateIssueCreated, isComplete, priority 
                            FROM projectIssues WHERE issueId = (?)"""
                            
        params = [issueId]
        record = self.cursor.execute(query, params).fetchone() 

        return createSingleRecordDictionary(record, self.cursor.description)
    
    # ========================================================================================
    
    def addNewIssue(self, issueInfo: dict) -> int:
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query = """INSERT INTO projectIssues (projectId, issueName, issueDescription, 
                                                dateIssueCreated, priority) 
                                                VALUES (?,?,?,?,?)"""
                                                
        params = [issueInfo["projectId"],
                issueInfo["issueName"],
                issueInfo["issueDescription"],
                issueInfo["dateIssueCreated"],
                issueInfo["priority"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
            self.cursor.execute("SELECT issueId FROM projectIssues WHERE issueId = LAST_INSERT_ROWID()")
            return self.cursor.fetchone()[0]
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================   

    def setTaskStatus(self, taskId: int, taskStatus):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query = "UPDATE projectTasks SET taskStatus = ? WHERE taskId = ?"
        params = [taskStatus, taskId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================
    
    def updateFeature(self, featureDict: dict):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query = "UPDATE projectFeatures SET featureName = ?, featureDescription = ?, priority = ? WHERE featureId = ?"
        params = [featureDict["featureName"], 
                featureDict["featureDescription"],                   
                featureDict["priority"], 
                featureDict["featureId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
        
    # ========================================================================================

    def updateCompleteFeature(self, featureId: int, isComplete: bool):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        complete = "True" if isComplete else "False"

        query = f"UPDATE projectFeatures SET featureCompleted = ? WHERE featureId = ?"
        params = [complete, featureId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
        
    # ========================================================================================
    

    def updateTask(self, taskDict: dict):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query  = "UPDATE projectTasks SET taskName = ?, taskDescription = ?, priority = ? WHERE taskId = ?"
        params = [taskDict["taskName"], 
                taskDict["taskDescription"], 
                taskDict["priority"], 
                taskDict["taskId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
        
    # ========================================================================================
            
    def updateCompleteTask(self, taskId: int, isComplete: bool):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        complete = "True" if isComplete else "False"

        query = f"UPDATE projectTasks SET isComplete = ? WHERE taskId = ?"
        params = [complete, taskId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
        
    # ========================================================================================
    
    def updateIssue(self, issueDict: dict):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query  = "UPDATE projectIssues SET issueName = ?, issueDescription = ?, priority = ? WHERE issueId = ?"
        params = [issueDict["issueName"],
                issueDict["issueDescription"],
                issueDict["priority"], 
                issueDict["issueId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
        
    # ========================================================================================
    
    def updateCompleteIssue(self, issueId: int, isComplete: bool):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        complete = "True" if isComplete else "False"

        query = f"UPDATE projectIssues SET isComplete = ? WHERE issueId = ?"
        params = [complete, issueId]

        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
        
    # ========================================================================================
    
    def deleteProject(self, projectId: int):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        self.cursor.execute(f"DELETE FROM projectIssues WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projectTasks WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projectFeatures WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projects WHERE projectId = '{projectId}'")
        self.connection.commit()
        
    # ========================================================================================
        
    def deleteFeature(self, featureId: int):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query  = "DELETE FROM projectFeatures WHERE featureId = (?)"
        params = [featureId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================
        
    def deleteTask(self, taskId: int):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query  = "DELETE FROM projectTasks WHERE taskId = (?)"
        params = [taskId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()

    # ========================================================================================
    
    def deleteIssue(self, issueId: int):
        self.viewController.log(self.viewController.debug, getCurrentFunction())
        # - - - - - - - - - - - - - - - -

        query  = "DELETE FROM projectIssues WHERE issueId = (?)"
        params = [issueId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            self.viewController.log(self.viewController.debug, f"An error occurred: {__class__.__name__}: {getCurrentFunction()}: {e}")
            self.connection.rollback()
            
    # ========================================================================================
    