##Sign up page

def test_loadPage(client):
    response = client.get("/changePass")
    assert b"<title>Sign up</title>" in response.data