import pytest
from ReqBase.models import Req
from ReqBase import db

## Update request page

@pytest.mark.usefixtures('login')
def test_updateRequest(client, app):
    
    client.post("/", 
                    data={
                        "appName": "TestApp", 
                        "appVendor": "Vendor", 
                        "reqName": "Requestor",     ##create a request
                        "archNum": "x64",
                        "note": "App notes"},
                        follow_redirects=True)
    
    client.post("/updateReq/1", 
                    data={
                        "appName": "EditApp", 
                        "appVendor": "EditVendor", 
                        "reqName": "EditRequestor",     ##edit the request
                        "archNum": "x86",
                        "note": "Edited App notes"},
                        follow_redirects=True)
    
    with app.app_context():
        assert db.session.get(Req, 1).app_name == "EditApp"  ##Checks the request has been created then been edited
        assert db.session.get(Req, 1).app_vendor == "EditVendor"
        assert db.session.get(Req, 1).req_name == "EditRequestor"
        assert db.session.get(Req, 1).arch == "x86"
        assert db.session.get(Req, 1).note == "Edited App notes"

