from pytest_bdd import scenario, given, when, then
import pytest

@scenario('logging.feature', 'Getting Application ID')
def test_GetApplicationId(application):
    pass

@given("I am a Logging user")
def LoggingUser():
    pass

@given("I have an application name")
def LoggingApplication(application):
    application.appName = "project_creator"

@when("I request an application ID")
def GetApplicationId(application):
    response = requests.get("http://<HOSTNAME>/loggingapi/v1/Application", json = {"appName": application.appName})
    data = response.json()
    application.appId = data["id"]
    assert data["status"] == 200

@then("I should get an application ID")
def CheckingForId(application):
    assert application.appId == 2