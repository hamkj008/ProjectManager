from icecream import ic
import sqlite3


# ========================================================================================
      

# Creates the database 

class ModelCreator:
   
    def __init__(self):
        ic("ModelCreator init")
        
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


    # ======================================================================================== 
    
    
    def firstTimeDatabaseInstall(self):
        ic("firstTimeDatabaseInstall")

        self.dropTables()
        self.createTables()


    # ========================================================================================
        

    def dropTables(self):
        ic("dropTables")
        
        self.cursor.execute("DROP TABLE IF EXISTS projectIssues")
        self.cursor.execute("DROP TABLE IF EXISTS projectTasks")
        self.cursor.execute("DROP TABLE IF EXISTS projectFeatures")
        self.cursor.execute("DROP TABLE IF EXISTS projects")
        self.connection.commit()


    # ========================================================================================


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
                            priority INTEGER DEFAULT 3 CHECK(priority IN(0, 1, 2, 3, 4)),
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
                            priority INTEGER DEFAULT 3 CHECK(priority IN(0, 1, 2, 3, 4)),
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
                            priority INTEGER DEFAULT 3 CHECK(priority IN(0, 1, 2, 3, 4)),
                            FOREIGN KEY(projectId) REFERENCES projects(projectId)
                        )""")
        
        self.connection.commit()


    # ========================================================================================