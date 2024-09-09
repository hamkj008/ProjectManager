import sqlite3
import os
from icecream import ic
from Models.ProjectModel import ProjectModel


# ========================================================================================

class DebugTestSetup:
   
    def __init__(self):

        dbFile = 'testplayground.db'
        self.connection = sqlite3.connect(dbFile)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()
        
        self.projectModel = ProjectModel(self.connection)    
       

    # ========================================================================================

    def setupDB(self):
    
        self.cursor.execute("DROP TABLE IF EXISTS projectIssues")
        self.cursor.execute("DROP TABLE IF EXISTS projectTasks")
        self.cursor.execute("DROP TABLE IF EXISTS projectFeatures")
        self.cursor.execute("DROP TABLE IF EXISTS projects")
        self.connection.commit()
    
        # -------------------------
    
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
    


    # ========================================================================================


    def projectObject(self):
    
        project = {"projectName"        : "Test Project",
                "projectDescription"    : "A test description",
                "dateCreated"           : "01-01-2014"} 
    
        return project

# ========================================================================================


    def featureObject(self):
    
        feature = {"projectId"              :   1,
                    "featureName"           :   "test feature",
                    "featureDescription"    :   "test feature description",
                    "dateFeatureCreated"    :   "02-02-2016",
                    "priority"              :     ""  }
    
        return feature


# ========================================================================================


    def taskObject(self):
    
        task = {"projectId"         :   1,
                "taskName"          :   "test task",
                "taskDescription"   :   "test task description",
                "dateTaskCreated"   :   "03-03-2017",
                "priority"          :     ""  }
    
        return task


# ========================================================================================


    def issueObject(self):
    
        issue = {"projectId"        :   1,
                "issueName"         :   "test issue",
                "issueDescription"  :   "test issue description",
                "dateIssueCreated"  :   "04-04-2018",
                "priority"          :     ""  }
    
        return issue
    

    # ========================================================================================

    # ========================================================================================


    def addProject(self): 
    
        projectId = self.projectModel.addNewProject(self.projectObject)
        return {"projectId" : projectId}
 
    # ========================================================================================   


    def addFeature(self): 
    
        featureId = self.projectModel.addNewFeature(self.featureObject)
        return {"featureId" : featureId}

    # ========================================================================================


    def addTask(self): 
    
        taskId = self.projectModel.addNewTask(self.taskObject)
        return {"taskId" : taskId}

    # ========================================================================================


    def addIssue(self): 
    
        issueId = self.projectModel.addNewIssue(self.issueObject)
        return {"issueId" : issueId}

    # ========================================================================================
    # ========================================================================================



    # # Add data to the database

    def populateDatabase(self): 
    
        project = self.projectModel.getProject(self.addProject["projectId"])    
        feature = self.projectModel.getFeature(self.addFeature["featureId"])
        task = self.projectModel.getTask(self.addTask["taskId"])    
        issue = self.projectModel.getIssue(self.addIssue["issueId"])
    
        return {
            "project"   : project,
            "feature"   : feature,
            "task"      : task,
            "issue"     : issue
        }

    # ========================================================================================


