import pytest

## Account page


def test_loadPageUnauthorized(client):

    response = client.get("/account")
    
    assert b"<title>Redirecting...</title>" in response.data   ##Checks page doesn't load when not logged in

@pytest.mark.usefixtures('login')
def test_loadPage(client):

    response = client.get("/account")

    assert b"<title>Account</title>" in response.data