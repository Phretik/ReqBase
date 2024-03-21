##Sign up page

def test_loadPage(client):
    response = client.get("/sign-up")
    assert b"<title>Sign up</title>" in response.data