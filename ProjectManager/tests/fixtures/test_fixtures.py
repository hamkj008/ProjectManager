import pytest

from tests.conftest import issueObject


# ========================================================================================

def test_addProject(projectModel, populateDatabase):

    project = projectModel.getProject(populateDatabase["project"]["projectId"])
    
    assert project is not None
    project["projectName"]          == "Test Project"
    project["projectDescription"]   == "A test description"
    project["dateCreated"]          == "01-01-2014"


# ========================================================================================

def test_addFeature(projectModel, populateDatabase):

    feature = projectModel.getFeature(populateDatabase["feature"]["featureId"])
    
    assert feature is not None
    feature["projectId"]            == 1
    feature["featureName"]          == "test feature"
    feature["featureDescription"]   == "test feature description"
    feature["dateFeatureCreated"]   == "02-02-2016"
    # feature["priority"]             == ""

# ========================================================================================

def test_addTask(projectModel, populateDatabase):

    task = projectModel.getTask(populateDatabase["task"]["taskId"])
    
    assert task is not None
    task["projectId"]           == 1
    task["taskName"]            == "test task"
    task["taskDescription"]     == "test task description"
    task["dateTaskCreated"]     == "03-03-2017"
    # task["priority"]            == ""


# ========================================================================================


def test_addIssue(projectModel, populateDatabase):

    issue = projectModel.getIssue(populateDatabase["issue"]["issueId"])
    
    assert issue is not None
    issue["projectId"]          == 1
    issue["issueName"]          == "test issue"
    issue["issueDescription"]   == "test issue description"
    issue["dateIssueCreated"]   == "04-04-2018"
    # issue["priority"]           == ""


# ========================================================================================
