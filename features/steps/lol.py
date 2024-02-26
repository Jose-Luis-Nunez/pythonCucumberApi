import pytest

@pytest.fixture
def application():
    helper = LoggingHelper()
    return helper

class LoggingHelper():
    appName = ""
    appId = None
    log = ""
    logStatus = None