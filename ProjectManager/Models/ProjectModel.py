from icecream import ic
import sqlite3
from MyHelperLibrary.Helpers.HelperMethods import createDictionary, createSingleRecordDictionary


# ========================================================================================
      

class ProjectModel:

    def __init__(self, connection=None):
        ic("ProjectModel init")
        
        self.connection = connection
        self.cursor = self.connection.cursor()


    # ========================================================================================


    def getProjectName(self, projectId):
        
        query = "SELECT projectName FROM projects WHERE projectId = (?)"
        params = [projectId]
        self.cursor.execute(query, params)
        
        return self.cursor.fetchone()[0]
    

    # ========================================================================================
    

    def getProjects(self, search=None):
        ic("getProjects")
        
        query = "SELECT projectId, projectName, projectDescription, dateCreated FROM projects"
        
        if search:
            query += " WHERE projectName LIKE (?)"
            
            # The comma , in the search indicates that it is part of a tuple. Without it there is an error.
            params = (f"%{search}%",)
            self.cursor.execute(query, params)
            
        else:
            self.cursor.execute(query)
                      
        rows = self.cursor.fetchall()
        resultsDictList = createDictionary(rows, self.cursor.description)

        return resultsDictList
    

    # ========================================================================================      
    

    def getProject(self, projectId):
        ic("getProject")
        
        query = """SELECT projectId, projectName, projectDescription, dateCreated 
                        FROM projects WHERE projectId = (?)"""
                        
        params = [projectId]
         
        self.cursor.execute(query, params)
        
        record = self.cursor.fetchone()  
        return createSingleRecordDictionary(record, self.cursor.description)
    

    # ========================================================================================      
    
    def addNewProject(self, projectInfo):
        
        params = [projectInfo["projectName"],
                    projectInfo["projectDescription"],
                    projectInfo["dateCreated"]]
        
        query = "INSERT INTO projects (projectName, projectDescription, dateCreated) VALUES (?,?,?)"
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
            self.cursor.execute("SELECT projectId FROM projects WHERE projectId = LAST_INSERT_ROWID()")
            return self.cursor.fetchone()[0]

        except sqlite3.Error as e:
            ic(f"An error occurred addNewProject: {e}")
            self.connection.rollback()


    # ========================================================================================   
    

    def updateProject(self, projectDict):

        query = "UPDATE projects SET projectName = ?, projectDescription = ? WHERE projectId = ?"
        params = [projectDict["projectName"], 
                projectDict["projectDescription"], 
                projectDict["projectId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateProject: {e}")
            self.connection.rollback()
       
            
    # ========================================================================================   
    

    def getFeatures(self, projectId, search=None):
        ic("getProjects")
        
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
        resultsDictList = createDictionary(rows, self.cursor.description)

        return resultsDictList
    

    # ========================================================================================
    

    def getFeature(self, featureId):
        ic("getProjects")
        
        query = """SELECT projectId, featureId, featureName, featureDescription, 
                            dateFeatureCreated, priority, featureCompleted 
                            FROM projectFeatures WHERE featureId = (?)"""
        
        params = [featureId]
        
        self.cursor.execute(query, params)
                      
        record = self.cursor.fetchone()  
        return createSingleRecordDictionary(record, self.cursor.description)
    

    # ========================================================================================
    

    def addNewFeature(self, featureInfo):
        
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
            ic(f"An error occurred addNewFeature: {e}")
            self.connection.rollback()


    # ========================================================================================   
    

    def getTasks(self, projectId, search=None):
        ic("getTasks")
        
        query = """SELECT projectId, taskId, taskName, taskDescription, dateTaskCreated, 
                    taskStatus, priority, isComplete 
                    FROM projectTasks WHERE projectId = (?)"""
                    
        params = [projectId]
        
        if search:
            query += f" AND taskName LIKE ?"            
            params.append(f"%{search}%")
            
        query += f" ORDER BY priority" 
            
        self.cursor.execute(query, params)
                      
        rows = self.cursor.fetchall()
        resultsDictList = createDictionary(rows, self.cursor.description)

        return resultsDictList
    

    # ========================================================================================
    

    def getTask(self, taskId):
        ic("getTasks")
        
        query = """SELECT projectId, taskId, taskName, taskDescription, dateTaskCreated, 
                    taskStatus, priority, isComplete 
                    FROM projectTasks WHERE taskId = (?)"""
                    
        params = [taskId]

        self.cursor.execute(query, params)
                      
        record = self.cursor.fetchone()  
        return createSingleRecordDictionary(record, self.cursor.description)
    

    # ========================================================================================
    

    def addNewTask(self, taskInfo):

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
            ic(f"An error occurred addNewTask: {e}")
            self.connection.rollback()


    # ========================================================================================   
    

    def getIssues(self, projectId, search=None):
        ic("getIssues")
        
        query = """SELECT projectId, issueId, issueName, issueDescription, 
                    dateIssueCreated, isComplete, priority 
                    FROM projectIssues WHERE projectId = (?)"""
                    
        params = [projectId]
        
        if search:
            query += f" AND issueName LIKE ?"
            params.append(f"%{search}%")
        
        query += f" ORDER BY priority"
        
        self.cursor.execute(query, params)
                      
        rows = self.cursor.fetchall()
        resultsDictList = createDictionary(rows, self.cursor.description)

        return resultsDictList
    
    
    # ========================================================================================
    
    def getIssue(self, issueId):
        ic("getIssues")
        
        query = """SELECT projectId, issueId, issueName, issueDescription, 
                            dateIssueCreated, isComplete, priority 
                            FROM projectIssues WHERE issueId = (?)"""
                            
        params = [issueId]

        self.cursor.execute(query, params)
           
        record = self.cursor.fetchone()  
        return createSingleRecordDictionary(record, self.cursor.description)
    
    
    # ========================================================================================
    

    def addNewIssue(self, issueInfo):
        
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
            ic(f"An error occurred addNewTask: {e}")
            self.connection.rollback()


    # ========================================================================================   


    def setTaskStatus(self, taskId, taskStatus):
        
        query = "UPDATE projectTasks SET taskStatus = ? WHERE taskId = ?"
        params = [taskStatus, taskId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred setTaskStatus: {e}")
            self.connection.rollback()


    # ========================================================================================
    

    def updateFeature(self, featureDict):

        query = "UPDATE projectFeatures SET featureName = ?, featureDescription = ?, priority = ? WHERE featureId = ?"
        params = [featureDict["featureName"], 
                featureDict["featureDescription"],                   
                featureDict["priority"], 
                featureDict["featureId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateFeature: {e}")
            self.connection.rollback()
        

    # ========================================================================================


    def updateCompleteFeature(self, featureId, isComplete):
        
        complete = "True" if isComplete else "False"

        query = f"UPDATE projectFeatures SET featureCompleted = ? WHERE featureId = ?"
        params = [complete, featureId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateCompleteFeature: {e}")
            self.connection.rollback()
        

    # ========================================================================================
    

    def updateTask(self, taskDict):

        query = "UPDATE projectTasks SET taskName = ?, taskDescription = ?, priority = ? WHERE taskId = ?"
        params = [taskDict["taskName"], 
                  taskDict["taskDescription"], 
                  taskDict["priority"], 
                  taskDict["taskId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateFeature: {e}")
            self.connection.rollback()
        

    # ========================================================================================
            

    def updateCompleteTask(self, taskId, isComplete):
        
        complete = "True" if isComplete else "False"

        query = f"UPDATE projectTasks SET isComplete = ? WHERE taskId = ?"
        params = [complete, taskId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateCompleteTask: {e}")
            self.connection.rollback()
        

    # ========================================================================================
    

    def updateIssue(self, issueDict):

        query = "UPDATE projectIssues SET issueName = ?, issueDescription = ?, priority = ? WHERE issueId = ?"
        params = [issueDict["issueName"],
                  issueDict["issueDescription"],
                  issueDict["priority"], 
                  issueDict["issueId"]]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateIssue: {e}")
            self.connection.rollback()
        

    # ========================================================================================
    

    def updateCompleteIssue(self, issueId, isComplete):
        
        complete = "True" if isComplete else "False"

        query = f"UPDATE projectIssues SET isComplete = ? WHERE issueId = ?"
        params = [complete, issueId]

        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred updateCompleteIssue: {e}")
            self.connection.rollback()
        
        
    # ========================================================================================
    

    def deleteProject(self, projectId):
        
        self.cursor.execute(f"DELETE FROM projectIssues WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projectTasks WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projectFeatures WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projects WHERE projectId = '{projectId}'")
        self.connection.commit()
        

    # ========================================================================================

        
    def deleteFeature(self, featureId):

        query = "DELETE FROM projectFeatures WHERE featureId = (?)"
        params = [featureId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred deleteTask: {e}")
            self.connection.rollback()


    # ========================================================================================
        

    def deleteTask(self, taskId):
        
        query = "DELETE FROM projectTasks WHERE taskId = (?)"
        params = [taskId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred deleteTask: {e}")
            self.connection.rollback()


    # ========================================================================================
    
    
    def deleteIssue(self, issueId):

        query = "DELETE FROM projectIssues WHERE issueId = (?)"
        params = [issueId]
        
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            
        except sqlite3.Error as e:
            ic(f"An error occurred deleteIssue: {e}")
            self.connection.rollback()
            

    # ========================================================================================
    