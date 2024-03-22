import pytest
from ReqBase.models import Log
from ReqBase import db


## Team log page


def test_loadPageUnauthorized(client):

    response = client.get("/teamLog")
    
    assert b"<title>Redirecting...</title>" in response.data   ##Checks page doesn't load when not logged in

@pytest.mark.usefixtures('login')
def test_loadPageLog(client):

    response = client.get("/teamLog")    ##Open team log page

    assert b"<title>Team Log</title>" in response.data   ##Check the page loads when logged in

@pytest.mark.usefixtures('login')
def test_createLog(client, app):

    response = client.post("/teamLog", 
                           data={
                               "log": "Test log"},       ##Post a log
                                follow_redirects=True)
    
    with app.app_context():
        assert Log.query.first().post == "Test log"    ##Check the log was posted