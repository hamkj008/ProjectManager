import pytest
from unittest.mock import Mock, MagicMock
from PySide6.QtWidgets import QApplication
from fixtures.fixture_databaseInit import db_connection, populateDatabase, addProject, addFeature, addTask, addIssue
from Models.ProjectModel import ProjectModel



# ========================================================================================

@pytest.fixture(scope="session")
def setupApp():
    app = QApplication([])
    yield app
    app.quit()
    
# ========================================================================================

@pytest.fixture
def viewControllerMock():
    return MagicMock()

# ========================================================================================

@pytest.fixture
def projectModel(db_connection):
    return ProjectModel(db_connection)

# ========================================================================================

@pytest.fixture
def projectObject():
    
    project = {"projectName"        : "Test Project",
            "projectDescription"    : "A test description",
            "dateCreated"           : "01-01-2014"} 
    
    return project

# ========================================================================================

@pytest.fixture
def featureObject():
    
    feature = {"projectId"              :   1,
                "featureName"           :   "test feature",
                "featureDescription"    :   "test feature description",
                "dateFeatureCreated"    :   "02-02-2016",
                "priority"              :     ""  }
    
    return feature



# ========================================================================================

@pytest.fixture
def taskObject():
    
    task = {"projectId"         :   1,
            "taskName"          :   "test task",
            "taskDescription"   :   "test task description",
            "dateTaskCreated"   :   "03-03-2017",
            "priority"          :     ""  }
    
    return task

# ========================================================================================

@pytest.fixture
def issueObject():
    
    issue = {"projectId"        :   1,
            "issueName"         :   "test issue",
            "issueDescription"  :   "test issue description",
            "dateIssueCreated"  :   "04-04-2018",
            "priority"          :     ""  }
    
    return issue

# ========================================================================================


