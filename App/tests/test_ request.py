import pytest
from ReqBase.models import Req
from ReqBase import db


## Request page


def test_loadPageUnauthorized(client):

    response = client.get("/")
    
    assert b"<title>Redirecting...</title>" in response.data   ##Checks page doesn't load when not logged in

@pytest.mark.usefixtures('login')
def test_loadPageRequest(client):

    response = client.get("/")           ##Open request page
    
    assert b"<title>Requests</title>" in response.data
            