from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager
    

db = SQLAlchemy() 
DB_NAME = "database.db"
DB_PATH = r'App\ReqBase\instance\database.db'


def create_app():
    app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates') ##Creates the flask app
    
    
    app.config['SECRET_KEY'] = 'Obliviate'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://reqbase_database_al0j_user:dmfgGcoJDLyPpvk8Rfmyz3aTNzAp9oBO@dpg-cnuid76d3nmc73aairog-a.oregon-postgres.render.com/reqbase_database_al0j"
    ##Sets Database URI
    
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')   ##Blueprints the URLs
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view= 'auth.login'  ##A library that allows the login and user functionality
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return db.session.get(User, int(id))
        ##return db.session.query(User).get(int(id))
        ##return User.query.get(int(id))     ##Loads user

    return app

def create_database(app):
    if not path.exists(DB_PATH):   ##Creates database unless one already exists
        with app.app_context():
            db.create_all()
