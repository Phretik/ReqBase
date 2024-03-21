##Sign up page

def test_loadPageUnauthorized(client):
    response = client.get("/changePass")
    assert b"<title>Redirecting...</title>" in response.data