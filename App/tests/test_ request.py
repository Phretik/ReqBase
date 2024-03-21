import pytest
from ReqBase.models import Req
from ReqBase import db

@pytest.mark.usefixtures('login')
def test_loadPage(client):
    response = client.get("/")
    assert b"<title>Requests</title>" in response.data

@pytest.mark.usefixtures('login')
def test_createRequest(client, app):

    response = client.post("/", 
                           data={
                               "appName": "TestApp", 
                               "appVendor": "Vendor", 
                               "reqName": "Requestor", 
                               "archNum": "x64",
                               "note": "App notes"},
                                follow_redirects=True)
    
    with app.app_context():
        assert Req.query.first().app_name == "TestApp"
            