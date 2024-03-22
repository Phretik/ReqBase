from ReqBase.models import User


## Sign in page


def test_loadPageSignUp(client):

    response = client.get("/sign-up")   ##Open sign up page

    assert b"<title>Sign up</title>" in response.data

def test_signUpUser(client, app):

    response = client.post("/sign-up", 
                           data={
                               "email": "Admin@admin.com",     ##Post sign up data listed
                               "firstname": "Admin", 
                               "password1": "password", 
                               "password2": "password"},
                                follow_redirects=True)
    
    with app.app_context():
        assert User.query.count() != 0    ##Assert user is created