import sqlite3
import os
import pytest
from icecream import ic


# ========================================================================================

@pytest.fixture
def db_connection():

    dbFile = 'test_db.db'
    connection = sqlite3.connect(dbFile)
    connection.execute("PRAGMA foreign_keys = OFF")
    cursor = connection.cursor()
    
    # Log foreign key constraints
    cursor.execute("PRAGMA foreign_keys")
    setting = cursor.fetchone()[0]
    ic(f"PRAGMA foreign_keys setting during test: {setting}")
    
    # ----------------------
    
    cursor.execute("DROP TABLE IF EXISTS projectIssues")
    cursor.execute("DROP TABLE IF EXISTS projectTasks")
    cursor.execute("DROP TABLE IF EXISTS projectFeatures")
    cursor.execute("DROP TABLE IF EXISTS projects")
    connection.commit()
    
    # -------------------------

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    projects( 
                        projectId INTEGER PRIMARY KEY,
                        projectName TEXT NOT NULL,
                        projectDescription TEXT,
                        dateCreated TEXT NOT NULL
                    )""")
        

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                    projectFeatures(   
                        featureId INTEGER PRIMARY KEY,
                        projectId INTEGER NOT NULL,
                        dateFeatureCreated TEXT NOT NULL,
                        featureName TEXT,
                        featureDescription TEXT,
                        priority INTEGER DEFAULT 3 CHECK(priority IN(1, 2, 3, 4, 5)),
                        FOREIGN KEY(projectId) REFERENCES projects(projectId)
                    )""")
        
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
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
        

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
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
        
    connection.commit()
    
    # -----------------
    
    yield connection  # Provide the connection to the test functions

    # -----------------
    
    # Teardown: Clean up database file
    cursor.close()
    connection.close()
    os.remove(dbFile)

# ========================================================================================

@pytest.fixture
def addProject(projectModel, projectObject): 
    
    projectId = projectModel.addNewProject(projectObject)
    return {"projectId" : projectId}
 
# ========================================================================================   

@pytest.fixture
def addFeature(projectModel, featureObject): 
    
    featureId = projectModel.addNewFeature(featureObject)
    return {"featureId" : featureId}

# ========================================================================================

@pytest.fixture
def addTask(projectModel, taskObject): 
    
    taskId = projectModel.addNewTask(taskObject)
    return {"taskId" : taskId}

# ========================================================================================

@pytest.fixture
def addIssue(projectModel, issueObject): 
    
    issueId = projectModel.addNewIssue(issueObject)
    return {"issueId" : issueId}

# ========================================================================================
# ========================================================================================



# # Add data to the database
@pytest.fixture
def populateDatabase(projectModel, addProject, addFeature, addTask, addIssue): 
    
    project = projectModel.getProject(addProject["projectId"])    
    feature = projectModel.getFeature(addFeature["featureId"])
    task = projectModel.getTask(addTask["taskId"])    
    issue = projectModel.getIssue(addIssue["issueId"])
    
    yield {
        "project"   : project,
        "feature"   : feature,
        "task"      : task,
        "issue"     : issue
    }

# ========================================================================================
 
