import pytest
from flask import Flask, request
from ReqBase import auth, db, DB_NAME, create_app
from ReqBase.models import User
from flask_login import login_user, login_required, logout_user, current_user

@pytest.fixture()
def app():
    app = create_app()
    app.config['SECRET_KEY'] = 'Obliviate'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def login(app, client):
    client.post("/sign-up", 
                           data={
                               "email": "Admin@admin.com", 
                               "firstname": "Admin", 
                               "password1": "password", 
                               "password2": "password"},
                                follow_redirects=True)
    
    response = client.post("/login", data={"email": "Admin@admin.com", "password": "password"})

    yield