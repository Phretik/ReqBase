from ReqBase.models import User
##Sign up page

def test_loadPage(client):
    response = client.get("/sign-up")
    assert b"<title>Sign up</title>" in response.data

def test_signUpUser(client, app):

    response = client.post("/sign-up", 
                           data={
                               "email": "Admin@admin.com", 
                               "firstname": "Admin", 
                               "password1": "password", 
                               "password2": "password"},
                                follow_redirects=True)
    
    with app.app_context():
        assert User.query.count() == 1