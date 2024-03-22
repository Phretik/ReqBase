import pytest

## Change password page


def test_loadPageUnauthorized(client):
    response = client.get("/changePass")
    assert b"<title>Redirecting...</title>" in response.data   ##Checks page doesn't load when not logged in

@pytest.mark.usefixtures('login')
def test_loadPageChangePswd(client):
    
    response = client.get("/changePass")         ##Check page loads when logged in

    assert b"<title>Change password</title>" in response.data