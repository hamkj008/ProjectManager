from icecream import ic
import sqlite3




class ProjectModel:
   
    def __init__(self):
        ic("Model init")
        
        self.connection = sqlite3.connect('projectManager.db')
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()
        

        # Check if the database has any data.
        self.cursor.execute("PRAGMA table_info({})".format("projects"))
        query = self.cursor.fetchall()
        

        # If the database does not exist, initialize first time install of the database
        if len(query) > 0:
            ic("database populated")
            
        else:  
            self.firstTimeDatabaseInstall()
           


    # ----------------------------------------------------------------------------------------


    def firstTimeDatabaseInstall(self):
        ic("firstTimeDatabaseInstall")

        self.dropTables()
        self.createTables()


    # ----------------------------------------------------------------------------------------
        

    def dropTables(self):
        ic("dropTables")
        
        self.cursor.execute("DROP TABLE IF EXISTS projectIssues")
        self.cursor.execute("DROP TABLE IF EXISTS projectTasks")
        self.cursor.execute("DROP TABLE IF EXISTS projectFeatures")
        self.cursor.execute("DROP TABLE IF EXISTS projects")
        self.connection.commit()


    # ----------------------------------------------------------------------------------------


    def createTables(self):
        ic("createTables")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        projects( 
                            projectId INTEGER PRIMARY KEY,
                            projectName TEXT NOT NULL,
                            projectDescription TEXT,
                            dateCreated TEXT NOT NULL
                        )""")
        

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        projectFeatures(   
                            featureId INTEGER PRIMARY KEY,
                            projectId INTEGER NOT NULL,
                            dateFeatureCreated TEXT NOT NULL,
                            featureName TEXT,
                            featureDescription TEXT,
                            priority INTEGER DEFAULT 3 CHECK(priority IN(1, 2, 3, 4, 5)),
                            FOREIGN KEY(projectId) REFERENCES projects(projectId)
                        )""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        projectTasks(   
                            taskId INTEGER PRIMARY KEY,
                            projectId INTEGER NOT NULL,
                            dateTaskCreated TEXT NOT NULL,
                            dateTaskStarted TEXT,
                            dateTaskFinished TEXT,
                            taskName TEXT,
                            taskDescription TEXT,
                            taskStatus TEXT DEFAULT 'Waiting' CHECK(taskStatus IN('Waiting', 'InProgress', 'Complete')),
                            isComplete TEXT DEFAULT 'False' CHECK(isComplete IN('True', 'False')),
                            priority INTEGER DEFAULT 3 CHECK(priority IN(1, 2, 3, 4, 5)),
                            FOREIGN KEY(projectId) REFERENCES projects(projectId)
                        )""")
        

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        projectIssues(   
                            issueId INTEGER PRIMARY KEY,
                            projectId INTEGER NOT NULL,
                            dateIssueCreated TEXT NOT NULL,
                            issueName TEXT,
                            issueDescription TEXT,
                            isComplete TEXT DEFAULT 'False' CHECK(isComplete IN('True', 'False')),
                            priority INTEGER DEFAULT 3 CHECK(priority IN(1, 2, 3, 4, 5)),
                            FOREIGN KEY(projectId) REFERENCES projects(projectId)
                        )""")
        
        self.connection.commit()


    # ----------------------------------------------------------------------------------------
     
    
    def getProjectName(self, projectId):
        
        self.cursor.execute(f"SELECT projectName FROM projects WHERE projectId = '{projectId}'")
        project = self.cursor.fetchone()[0]

        return project
    

    # ----------------------------------------------------------------------------------------
    
    def getProjects(self, search=None):
        ic("getProjects")
        
        query = "SELECT projectId, projectName, projectDescription, dateCreated FROM projects"
        
        if search:
            query += " WHERE (projectName LIKE ?)"
            
            # The comma , in the search indicates that it is part of a tuple. Without it there is an error.
            queryParams = (f"%{search}%",)
            self.cursor.execute(query, queryParams)
            
        else:
            self.cursor.execute(query)
                      
        rows = self.cursor.fetchall()
        

        # -- Create dictionary --
        columnNames = [description[0] for description in self.cursor.description]

        resultsDictList = []

        # Zip the column names and results together into a dictionary list
        for row in rows:
            rowDict = {}
            for columnName, value in zip(columnNames, row):
                rowDict[columnName] = value
            resultsDictList.append(rowDict)

        return resultsDictList
    

    # ----------------------------------------------------------------------------------------      
    

    def addNewProject(self, projectInfo):
        
        projectName = projectInfo["projectName"]
        projectDescription = projectInfo["projectDescription"]
        dateCreated = projectInfo["dateCreated"]
        
        self.cursor.execute(f"""INSERT INTO projects (projectName, projectDescription, dateCreated) VALUES (
                            '{projectName}', 
                            '{projectDescription}', 
                            '{dateCreated}')""")

        self.connection.commit()
       

    # ----------------------------------------------------------------------------------------   
    

    def addNewFeature(self, featureInfo):
        
        projectId = featureInfo["projectId"]
        featureName = featureInfo["featureName"]
        featureDescription = featureInfo["featureDescription"]
        dateFeatureCreated = featureInfo["dateFeatureCreated"]
        priority = featureInfo["priority"]
        
        self.cursor.execute(f"""INSERT INTO projectFeatures (projectId, featureName, featureDescription, dateFeatureCreated, priority) VALUES (
                            '{projectId}', 
                            '{featureName}', 
                            '{featureDescription}', 
                            '{dateFeatureCreated}',
                            '{priority}')""")

        self.connection.commit()
       

    # ----------------------------------------------------------------------------------------   
    

    def addNewTask(self, taskInfo):
        
        projectId = taskInfo["projectId"]
        taskName = taskInfo["taskName"]
        taskDescription = taskInfo["taskDescription"]
        dateTaskCreated = taskInfo["dateTaskCreated"]
        priority = taskInfo["priority"]
        
        self.cursor.execute(f"""INSERT INTO projectTasks (projectId, taskName, taskDescription, dateTaskCreated, priority) VALUES (
                            '{projectId}',
                            '{taskName}', 
                            '{taskDescription}', 
                            '{dateTaskCreated}',
                            '{priority}')""")

        self.connection.commit()
       

    # ----------------------------------------------------------------------------------------   
    

    def addNewIssue(self, issueInfo):
        
        projectId = issueInfo["projectId"]
        issueName = issueInfo["issueName"]
        issueDescription = issueInfo["issueDescription"]
        dateIssueCreated = issueInfo["dateIssueCreated"]
        priority = issueInfo["priority"]
        
        self.cursor.execute(f"""INSERT INTO projectIssues (projectId, issueName, issueDescription, dateIssueCreated, priority) VALUES (
                            '{projectId}',
                            '{issueName}', 
                            '{issueDescription}', 
                            '{dateIssueCreated}',
                            '{priority}')""")

        self.connection.commit()
       

    # ----------------------------------------------------------------------------------------   


    def getFeatures(self, search=None):
        ic("getProjects")
        
        query = "SELECT projectId, featureId, featureName, featureDescription, dateFeatureCreated, priority FROM projectFeatures"
        
        if search:
            query += f" WHERE featureName LIKE %{search}%"            
            
        query += f" ORDER BY priority" 
        
        self.cursor.execute(query)
                      
        rows = self.cursor.fetchall()
        
        resultsDictList = self.createDictionary(rows)

        return resultsDictList
    

    # ----------------------------------------------------------------------------------------


    def getTasks(self, search=None):
        ic("getTasks")
        
        query = "SELECT projectId, taskId, taskName, taskDescription, dateTaskCreated, taskStatus, priority, isComplete FROM projectTasks"
        
        if search:
            query += f" WHERE taskName LIKE %{search}%"            
            
        query += f" ORDER BY priority" 
            
        self.cursor.execute(query)
                      
        rows = self.cursor.fetchall()

        resultsDictList = self.createDictionary(rows)

        return resultsDictList
    

    # ----------------------------------------------------------------------------------------


    def getIssues(self, search=None):
        ic("getIssues")
        
        query = "SELECT projectId, issueId, issueName, issueDescription, dateIssueCreated, isComplete, priority FROM projectIssues"
        
        if search:
            query += f" WHERE issueName LIKE %{search}%"
        
        query += f" ORDER BY priority"
        
        self.cursor.execute(query)
                      
        rows = self.cursor.fetchall()

        resultsDictList = self.createDictionary(rows)

        return resultsDictList
    
    
    # ----------------------------------------------------------------------------------------
    

    def createDictionary(self, rows):
        
         # -- Create dictionary --
        columnNames = [description[0] for description in self.cursor.description]

        resultsDictList = []

        # Zip the column names and results together into a dictionary list
        for row in rows:
            rowDict = {}
            for columnName, value in zip(columnNames, row):
                rowDict[columnName] = value
            resultsDictList.append(rowDict)

        return resultsDictList
     

    # ----------------------------------------------------------------------------------------


    def setTaskStatus(self, projectId, taskId, taskStatus):
        
        self.cursor.execute(f"UPDATE projectTasks SET taskStatus = '{taskStatus}' WHERE projectId = '{projectId}' AND taskId = '{taskId}'")
        self.connection.commit()
        
    # ----------------------------------------------------------------------------------------
    
    
    def setIssueStatus(self, projectId, issueId, issueStatus):
        
        self.cursor.execute(f"UPDATE projectIssues SET isComplete = '{issueStatus}' WHERE projectId = '{projectId}' AND issueId = '{issueId}'")
        self.connection.commit()


    # ----------------------------------------------------------------------------------------
    
    
    def updateCompleteTask(self, projectId, taskId, isComplete):
        
        self.cursor.execute(f"UPDATE projectTasks SET isComplete = '{isComplete}' WHERE projectId = '{projectId}' AND taskId = '{taskId}'")
        self.connection.commit()
        
        
    # ----------------------------------------------------------------------------------------
    
    
    def updateCompleteIssue(self, projectId, issueId, isComplete):
        
        self.cursor.execute(f"UPDATE projectIssues SET isComplete = '{isComplete}' WHERE projectId = '{projectId}' AND issueId = '{issueId}'")
        self.connection.commit()
        
        
    # ----------------------------------------------------------------------------------------
    
    def deleteProject(self, projectId):
        
        self.cursor.execute(f"DELETE FROM projectIssues WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projectTasks WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projectFeatures WHERE projectId = '{projectId}'")
        self.cursor.execute(f"DELETE FROM projects WHERE projectId = '{projectId}'")
        self.connection.commit()
        

    # ----------------------------------------------------------------------------------------

        
    def deleteFeature(self, projectId, featureId):
        
        self.cursor.execute(f"DELETE FROM projectFeatures WHERE projectId = '{projectId}' AND featureId = '{featureId}'")
        self.connection.commit()
        

    # ----------------------------------------------------------------------------------------
        

    def deleteTask(self, projectId, taskId):
        
        self.cursor.execute(f"DELETE FROM projectTasks WHERE projectId = '{projectId}' AND taskId = '{taskId}'")
        self.connection.commit()
        

    # ----------------------------------------------------------------------------------------
    
    
    def deleteIssue(self, projectId, issueId):
        
        self.cursor.execute(f"DELETE FROM projectIssues WHERE projectId = '{projectId}' AND issueId = '{issueId}'")
        self.connection.commit()