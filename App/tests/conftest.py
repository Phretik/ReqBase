import pytest
from flask import Flask, request
from ReqBase import auth, db, DB_NAME
from ReqBase.models import User
from App import create_app

@pytest.fixture()
def app():
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()