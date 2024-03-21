import pytest
from flask import Flask, request
from ReqBase import auth, db, DB_NAME
from ReqBase.models import User

def test_signup(client):
    response = client.get("/sign-up")
    assert b"<title>Sign up</title>" in response.data