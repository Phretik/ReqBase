from flask_login import current_user


## Login page


def test_loadPageLogin(client):   

    response = client.get("/login")  ##Open Login page

    assert b"<title>Login</title>" in response.data  

    ## No need to test login ability as almost all pages require login before their tests work
