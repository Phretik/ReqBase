##Sign up page

def test_loadPage(client):
    response = client.get("/login")
    assert b"<title>Login</title>" in response.data